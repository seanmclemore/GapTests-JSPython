/// <reference types="cypress" />

describe('my form', () => {
  let user = "shopmanager"
  let pass = "axY2rimcSzO9cobfAZBwNLnX"
  let productId = 0
  let quantity = 7
  let requestBody = {
    name:"seanMclemore",
    type: "simple",
    regular_price: "31.99",
    description: "Horse for children between 3 and 5 years old",
    short_description: "Horse",
    categories: [
      {
          name: "Toys",
          slug: "toy-cat"
      }
    ],  
    images: [
      {
        src: "https://themes.woocommerce.com/homestore/wp-content/uploads/sites/88/2015/11/toys-4-e1448555965427.jpg"
      }
    ]
  }

  before(() => {
    cy.request({
      url: 'http://34.205.174.166/wp-json/wc/v3/products',
      method: 'POST',
      auth: {
        username: user,
        password: pass
      },
      form: true, 
      body: requestBody
    }).then((response) => {
      expect(response.body).property('id').to.not.be.oneOf([null, ""])
      const responseBody = response.body
      productId = responseBody['id']
    });
  })

  it('Navigate to the page of the product', () => {
    cy.visit('http://34.205.174.166/product/' + requestBody['name'])
    cy.get('h1.product_title.entry-title').contains(requestBody['name'])
    cy.get('.woocommerce-Price-amount.amount').contains(requestBody['regular_price'])

    cy.get('[name="quantity"]').clear().type(quantity)

    cy.get('[name="add-to-cart"]').click()
    cy.get('.cart-contents').children('span.count').contains(quantity + ' items')

    cy.get('#site-header-cart').click()
    cy.get('table.shop_table').contains('td.product-name', requestBody['name'])
      .siblings('td.product-price').contains(requestBody['regular_price']).parent('td.product-price')
      .siblings('td.product-quantity').find('input').should('have.value', quantity)
  })

  after(() => {
    cy.request({
      url: 'http://34.205.174.166/wp-json/wc/v3/products/' + productId,
      method: 'DELETE',
      auth: {
        username: user,
        password: pass
      }
    })
  })
})