# Ecommerce App Back-End 

This project was developed for the software development course of mine during my Masters. It aims to provide APIs to add,update,delete products functionality
on the seller side. On the buyer side, it provides functionalities such as add to cart, checkout, search. It is hosted on http://arefin4414.pythonanywhere.com/

### Type of users
There are two kinds of users, maintained under one user. To maintain them seperate API endpoints, serializer methods are used. 
A seller only can create companies, categories. When adding products, he has to choose them.

## Endpoints
- Admin Panel: http://arefin4414.pythonanywhere.com/admin/
- Create buyer user and listing API (POST,GET): http://arefin4414.pythonanywhere.com/buyers/

Sample creation Payload for Buyer User Creation
```
{
  firstname:"sample firstname",
  last_name:"sample lastname",
  password:"12345678",
  username:"s1",
  email:"a@a.com",
  address: Check address section
}
optional parameter: address
```
- Update buyer user, detail, delete API (PUT,DELETE, GET): http://arefin4414.pythonanywhere.com/buyers/buyer_id/
```
buyer_id: any valid buyer id
fields: any fields except the email can be updated. Check the Sample payload for buyer creation
```
- Create Seller user and listing API (POST,GET): http://arefin4414.pythonanywhere.com/sellers/

Sample creation Payload for Seller User Creation
```
{
  firstname:"sample firstname",
  last_name:"sample lastname",
  password:"12345678",
  photo_id_num:"A1",
  email:"a@a.com"
}
photo_id_num: Number of a photo ID of a government issue ID. For now, it does not have any validation, provide anything
```


- Update seller user, detail, delete API (PUT,DELETE, GET): http://arefin4414.pythonanywhere.com/sellers/seller_id/
```
seller_id: any valid seller id
fields: any fields except the email can be updated. Check the Sample payload for seller creation
```


- Create Company and listing API (POST,GET): http://arefin4414.pythonanywhere.com/companies/

Sample creation Payload for Company Creation
```
{
  company_name:"sample name",
  company_username:"sample lastname",
  address:check address payload section
}

```

- Update company, detail, delete API (PUT,DELETE, GET): http://arefin4414.pythonanywhere.com/companies/company_id/
```
company_id: any valid company id
```



- Create Address and listing API (POST,GET): http://arefin4414.pythonanywhere.com/addresses/

Sample creation Payload for Address Creation
```
{
  street_address:"sample",
  city:"sample ",
  province: "sk",
  zipcode: "s4s0hh"
}
```


- Update address, detail, delete API (PUT,DELETE, GET): http://arefin4414.pythonanywhere.com/addresses/address_id/
```
address_id: any valid address id
```

- Create Category and listing API (POST,GET): http://arefin4414.pythonanywhere.com/categories/

Sample creation Payload for Category Creation
```
{
  name:"sample"
}
```


- Update category, detail, delete API (PUT,DELETE, GET): http://arefin4414.pythonanywhere.com/categories/category_id/
```
category_id: any valid category id
deleting a category will delete all products associated with it. Be cautious
```

- Create Product and listing API (POST,GET): http://arefin4414.pythonanywhere.com/products/

Sample creation Payload for Product Creation
```
{
  name:"sample name",
  price:2,
  quanitity:10,
  delivery_cost:5,
  category_id:1,
  company_id: 2,
  seller_id:1
}
```


- Update product , detail, delete API (PUT,DELETE, GET): http://arefin4414.pythonanywhere.com/products/product_id/
```
product_id: any valid product's id
```

- Product Search API (GET): http://arefin4414.pythonanywhere.com/products-by-search-keywords/keyword/
```
keyword: search keywords, do not include space for now
```

- Products of a specific seller (GET): http://arefin4414.pythonanywhere.com/products-by-seller/seller_id/
```
seller_id: any valid seller id
```

- Products of a specific category (GET): http://arefin4414.pythonanywhere.com/products-by-category/category_name/
```
category_name: any valid category name, do not send spaced names for now
```

- Products of a specific company (GET): http://arefin4414.pythonanywhere.com/products-by-company/company_id/
```
company_id: any valid company ID
```

- Create Review and listing API (POST,GET): http://arefin4414.pythonanywhere.com/reviews/

Sample creation Payload for Review Creation
```
{
  buyer_user_id:1,
  product_id:1,
  description:"sample description"
}
```


- Update review , detail, delete API (PUT,DELETE, GET): http://arefin4414.pythonanywhere.com/reviews/review_id/
```
review_id: any valid review's id
```

- Create Orderline and listing API (POST,GET): http://arefin4414.pythonanywhere.com/order-lines/

Sample creation Payload for Orderline Creation
```
{
  order_id:1,
  product_id:1,
  quantity:1
}
```


- Update Orderline , detail, delete API (PUT,DELETE, GET): http://arefin4414.pythonanywhere.com/order-lines/orderline_id/
```
orderline_id: any valid orderline's ID
```

- Create Order and listing API (POST,GET): http://arefin4414.pythonanywhere.com/orders/

Sample creation Payload for Order Creation
```
{
  buyer_user_id:1,
  billing_firstname:"a",
  billing_lastname:"b",
  billing_email:"a@a.com",
  billing_contact_number:"30655555",
  value:15,
  delivered:false
}
```


- Update order , detail, delete API (PUT,DELETE, GET): http://arefin4414.pythonanywhere.com/orders/order_id/
```
order_id: any valid order's ID
```

- An order with the orderlines associated with it, Orderdetails with orderlines (GET): http://arefin4414.pythonanywhere.com/order-with-orderlines/order_id/
```
order_id: any valid order ID
```

- Orders List with orderlines of a specified user (GET): http://arefin4414.pythonanywhere.com/order-orderlines-by-user/user_id/
```
user_id: any valid user ID
```

- Create Cartline and listing API (POST,GET): http://arefin4414.pythonanywhere.com/cartlines/

Sample creation Payload for Cartline Creation
```
{
  cart_id:1,
  product_id:1,
  quantity:1
}
```


- Update Cartline , detail, delete API (PUT,DELETE, GET): http://arefin4414.pythonanywhere.com/cartlines/cartline_id/
```
cartline_id: any valid cartline's ID
```

- Create Cart and listing API (POST,GET): http://arefin4414.pythonanywhere.com/carts/

Sample creation Payload for Cart Creation
```
{
  user_id:1
}
```


- Update cart , detail, delete API (PUT,DELETE, GET): http://arefin4414.pythonanywhere.com/carts/cart_id/
```
cart_id: any valid cart's ID
```

- Cart with cartlines of a specified user (GET): http://arefin4414.pythonanywhere.com/cart-carlines-by-user/user_id/
```
user_id: any valid user ID
one user can have only one cart
```

- add to cart API (POST): http://arefin4414.pythonanywhere.com/add-to-cart-user/
Sample creation Payload for Add to Cart
```
{
  user_id:1,
  product_id:1
}
```

- API that checks username and password and user type and returns user information with token (Login and then return token)
Login state is not saved for now, just a token is returned, if the all the information matches against a user. This token would be required to call API, in future I 
would do this.
http://arefin4414.pythonanywhere.com/get-auth-token/
Sample creation Payload to get the token and the user
```
{
  email:"a@a.com,
  password:"12345678",
  is_buyer:false
}
```

## Responses:
Here are the responses of the API are posted
- Buyer detail( for the Buyer List API, a list will be returned with this type of item)
```
address can be Null when the buyer is first created, as the address is optional when creating the buyer
{
    "first_name": "asda234",
    "last_name": "asd",
    "email": "dd@dd.com",
    "username": "user111",
    "address": {
        "id": 5,
        "street_address": "adasd",
        "city": "asdad",
        "province": "asd",
        "zipcode": "asdasd"
    },
    "pk": 2
}
```
- Seller detail( for the Seller List API, a list will be returned with this type of item)
```
{
    "first_name": "karima",
    "last_name": "seller",
    "email": "b@a.com",
    "photo_id_num": "idnum12",
    "pk": 8
}
```


- Company detail ( for the Company List API, a list will be returned with this type of item)
```
{
    "company_name": "company10",
    "company_username": "username41",
    "address": {
        "id": 2,
        "street_address": "abcd",
        "city": "Regina",
        "province": "sk",
        "zipcode": "abc"
    },
    "pk": 1
}
```

- Address detail ( for the Address List API, a list will be returned with this type of item)
```
{
    "id": 2,
    "street_address": "abcd",
    "city": "Regina",
    "province": "sk",
    "zipcode": "abc"
}
```

- Product detail ( for the Product List API, a list will be returned with this type of item)
```
{
    "name": "product10888",
    "price": 1.0,
    "quantity": 20,
    "delivery_cost": 1.0,
    "category": {
        "name": "Tech",
        "pk": 1
    },
    "company": {
        "company_name": "company10",
        "company_username": "username41",
        "address": {
            "id": 2,
            "street_address": "abcd",
            "city": "Regina",
            "province": "sk",
            "zipcode": "abc"
        },
        "pk": 1
    },
    "seller": {
        "first_name": "shamsul",
        "last_name": "arefin",
        "email": "a@a.com",
        "photo_id_num": null,
        "pk": 1
    },
    "date": "2021-10-26T11:36:40.526778Z",
    "pk": 4
}
```

- Review detail ( for the Review List API, a list will be returned with this type of item)
```
{
    "user": {
        "first_name": "shamsul",
        "last_name": "arefin",
        "email": "a@a.com",
        "username": "dfsdf",
        "address": null,
        "pk": 1
    },
    "description": "review 2 Excelent product",
    "product": {
        "name": "product10888",
        "price": 1.0,
        "quantity": 20,
        "delivery_cost": 1.0,
        "category": {
            "name": "Tech",
            "pk": 1
        },
        "company": {
            "company_name": "company10",
            "company_username": "username41",
            "address": {
                "id": 2,
                "street_address": "abcd",
                "city": "Regina",
                "province": "sk",
                "zipcode": "abc"
            },
            "pk": 1
        },
        "seller": {
            "first_name": "shamsul",
            "last_name": "arefin",
            "email": "a@a.com",
            "photo_id_num": null,
            "pk": 1
        },
        "date": "2021-10-26T11:36:40.526778Z",
        "pk": 4
    },
    "pk": 1
}
```

- Order detail ( for the Order List API, a list will be returned with this type of item)
```
{
    "unique_order_id": "24B46B",
    "buyer": {
        "first_name": "shamsul",
        "last_name": "arefin",
        "email": "a@a.com",
        "username": "dfsdf",
        "address": null,
        "pk": 1
    },
    "date": "2021-10-18T21:08:41.000310Z",
    "value": 15.0,
    "billing_firstname": "aa",
    "billing_lastname": "bb",
    "billing_email": "aa@aa.com",
    "billing_contact_number": "511515",
    "delivered": false,
    "pk": 1
}
```

- Orderline detail ( for the orderlines List API, a list will be returned with this type of item)
```
{
    "product": {
        "name": "productui0",
        "price": 2.0,
        "quantity": 2,
        "delivery_cost": 2.0,
        "category": {
            "name": "Tech",
            "pk": 1
        },
        "company": {
            "company_name": "company10",
            "company_username": "username41",
            "address": {
                "id": 2,
                "street_address": "abcd",
                "city": "Regina",
                "province": "sk",
                "zipcode": "abc"
            },
            "pk": 1
        },
        "seller": {
            "first_name": "karima",
            "last_name": "seller",
            "email": "b@a.com",
            "photo_id_num": "idnum12",
            "pk": 8
        },
        "date": "2021-10-27T09:23:29.049307Z",
        "pk": 6
    },
    "quantity": 3,
    "order": {
        "unique_order_id": "0B0C23",
        "buyer": {
            "first_name": "asda234",
            "last_name": "asd",
            "email": "dd@dd.com",
            "username": "user111",
            "address": {
                "id": 5,
                "street_address": "adasd",
                "city": "asdad",
                "province": "asd",
                "zipcode": "asdasd"
            },
            "pk": 2
        },
        "date": "2021-11-01T15:53:41.150080Z",
        "value": 13.0,
        "billing_firstname": "asda",
        "billing_lastname": "asd",
        "billing_email": "dd@dd.com",
        "billing_contact_number": "3065396709",
        "delivered": false,
        "pk": 4
    },
    "pk": 4
}
```

- Cart detail ( for the Cart List API, a list will be returned with this type of item)
```
{
    "unique_id": "unique4",
    "user": {
        "first_name": "asda234",
        "last_name": "asd",
        "email": "dd@dd.com",
        "username": "user111",
        "address": {
            "id": 5,
            "street_address": "adasd",
            "city": "asdad",
            "province": "asd",
            "zipcode": "asdasd"
        },
        "pk": 2
    },
    "pk": 1
}
```

- Cartline detail ( for the Cartline List API, a list will be returned with this type of item)
```
{
    "product": {
        "name": "product10888",
        "price": 1.0,
        "quantity": 20,
        "delivery_cost": 1.0,
        "category": {
            "name": "Tech",
            "pk": 1
        },
        "company": {
            "company_name": "company10",
            "company_username": "username41",
            "address": {
                "id": 2,
                "street_address": "abcd",
                "city": "Regina",
                "province": "sk",
                "zipcode": "abc"
            },
            "pk": 1
        },
        "seller": {
            "first_name": "shamsul",
            "last_name": "arefin",
            "email": "a@a.com",
            "photo_id_num": null,
            "pk": 1
        },
        "date": "2021-10-26T11:36:40.526778Z",
        "pk": 4
    },
    "cart": {
        "unique_id": "unique4",
        "user": {
            "first_name": "tanjim",
            "last_name": "tanjim",
            "email": "tanjim@tanjim.com",
            "username": "tanjim123",
            "address": null,
            "pk": 9
        },
        "pk": 2
    },
    "quantity": 8,
    "pk": 3
}
```

- Cart with the Cartlines Response by a specific User: This will give the current cart information, cartlines of a user
```
cartlines can be null when a user has not added anything to the cart
{
    "unique_id": "unique4",
    "user": {
        "first_name": "tanjim",
        "last_name": "tanjim",
        "email": "tanjim@tanjim.com",
        "username": "tanjim123",
        "address": null,
        "pk": 9
    },
    "cartlines": [
        {
            "product": {
                "name": "product10888",
                "price": 1.0,
                "quantity": 20,
                "delivery_cost": 1.0,
                "category": {
                    "name": "Tech",
                    "pk": 1
                },
                "company": {
                    "company_name": "company10",
                    "company_username": "username41",
                    "address": {
                        "id": 2,
                        "street_address": "abcd",
                        "city": "Regina",
                        "province": "sk",
                        "zipcode": "abc"
                    },
                    "pk": 1
                },
                "seller": {
                    "first_name": "shamsul",
                    "last_name": "arefin",
                    "email": "a@a.com",
                    "photo_id_num": null,
                    "pk": 1
                },
                "date": "2021-10-26T11:36:40.526778Z",
                "pk": 4
            },
            "cart": {
                "unique_id": "unique4",
                "user": {
                    "first_name": "tanjim",
                    "last_name": "tanjim",
                    "email": "tanjim@tanjim.com",
                    "username": "tanjim123",
                    "address": null,
                    "pk": 9
                },
                "pk": 2
            },
            "quantity": 8,
            "pk": 3
        }
    ],
    "pk": 2
}
```

- Order list with orderlines for a specified user: calling the API will give you the order list with the orderlines, of a specific user
```
[
    {
        "unique_order_id": "BB5C9D",
        "buyer": {
            "first_name": "asda234",
            "last_name": "asd",
            "email": "dd@dd.com",
            "username": "user111",
            "address": {
                "id": 5,
                "street_address": "adasd",
                "city": "asdad",
                "province": "asd",
                "zipcode": "asdasd"
            },
            "pk": 2
        },
        "date": "2021-11-01T15:47:21.546794Z",
        "value": 4.0,
        "billing_firstname": "asda",
        "billing_lastname": "asd",
        "billing_email": "dd@dd.com",
        "billing_contact_number": "3065396709",
        "delivered": false,
        "pk": 3,
        "orderlines": [],
        "quantity": 0
    },
    {
        "unique_order_id": "0B0C23",
        "buyer": {
            "first_name": "asda234",
            "last_name": "asd",
            "email": "dd@dd.com",
            "username": "user111",
            "address": {
                "id": 5,
                "street_address": "adasd",
                "city": "asdad",
                "province": "asd",
                "zipcode": "asdasd"
            },
            "pk": 2
        },
        "date": "2021-11-01T15:53:41.150080Z",
        "value": 13.0,
        "billing_firstname": "asda",
        "billing_lastname": "asd",
        "billing_email": "dd@dd.com",
        "billing_contact_number": "3065396709",
        "delivered": false,
        "pk": 4,
        "orderlines": [
            {
                "product": {
                    "name": "product10888",
                    "price": 1.0,
                    "quantity": 20,
                    "delivery_cost": 1.0,
                    "category": {
                        "name": "Tech",
                        "pk": 1
                    },
                    "company": {
                        "company_name": "company10",
                        "company_username": "username41",
                        "address": {
                            "id": 2,
                            "street_address": "abcd",
                            "city": "Regina",
                            "province": "sk",
                            "zipcode": "abc"
                        },
                        "pk": 1
                    },
                    "seller": {
                        "first_name": "shamsul",
                        "last_name": "arefin",
                        "email": "a@a.com",
                        "photo_id_num": null,
                        "pk": 1
                    },
                    "date": "2021-10-26T11:36:40.526778Z",
                    "pk": 4
                },
                "quantity": 1,
                "order": {
                    "unique_order_id": "0B0C23",
                    "buyer": {
                        "first_name": "asda234",
                        "last_name": "asd",
                        "email": "dd@dd.com",
                        "username": "user111",
                        "address": {
                            "id": 5,
                            "street_address": "adasd",
                            "city": "asdad",
                            "province": "asd",
                            "zipcode": "asdasd"
                        },
                        "pk": 2
                    },
                    "date": "2021-11-01T15:53:41.150080Z",
                    "value": 13.0,
                    "billing_firstname": "asda",
                    "billing_lastname": "asd",
                    "billing_email": "dd@dd.com",
                    "billing_contact_number": "3065396709",
                    "delivered": false,
                    "pk": 4
                },
                "pk": 2
            },
            {
                "product": {
                    "name": "product from the ui1",
                    "price": 1.0,
                    "quantity": 1,
                    "delivery_cost": 1.0,
                    "category": {
                        "name": "Tech",
                        "pk": 1
                    },
                    "company": {
                        "company_name": "company10",
                        "company_username": "username41",
                        "address": {
                            "id": 2,
                            "street_address": "abcd",
                            "city": "Regina",
                            "province": "sk",
                            "zipcode": "abc"
                        },
                        "pk": 1
                    },
                    "seller": {
                        "first_name": "karima",
                        "last_name": "seller",
                        "email": "b@a.com",
                        "photo_id_num": "idnum12",
                        "pk": 8
                    },
                    "date": "2021-10-27T09:04:28.130946Z",
                    "pk": 5
                },
                "quantity": 2,
                "order": {
                    "unique_order_id": "0B0C23",
                    "buyer": {
                        "first_name": "asda234",
                        "last_name": "asd",
                        "email": "dd@dd.com",
                        "username": "user111",
                        "address": {
                            "id": 5,
                            "street_address": "adasd",
                            "city": "asdad",
                            "province": "asd",
                            "zipcode": "asdasd"
                        },
                        "pk": 2
                    },
                    "date": "2021-11-01T15:53:41.150080Z",
                    "value": 13.0,
                    "billing_firstname": "asda",
                    "billing_lastname": "asd",
                    "billing_email": "dd@dd.com",
                    "billing_contact_number": "3065396709",
                    "delivered": false,
                    "pk": 4
                },
                "pk": 3
            },
            {
                "product": {
                    "name": "productui0",
                    "price": 2.0,
                    "quantity": 2,
                    "delivery_cost": 2.0,
                    "category": {
                        "name": "Tech",
                        "pk": 1
                    },
                    "company": {
                        "company_name": "company10",
                        "company_username": "username41",
                        "address": {
                            "id": 2,
                            "street_address": "abcd",
                            "city": "Regina",
                            "province": "sk",
                            "zipcode": "abc"
                        },
                        "pk": 1
                    },
                    "seller": {
                        "first_name": "karima",
                        "last_name": "seller",
                        "email": "b@a.com",
                        "photo_id_num": "idnum12",
                        "pk": 8
                    },
                    "date": "2021-10-27T09:23:29.049307Z",
                    "pk": 6
                },
                "quantity": 3,
                "order": {
                    "unique_order_id": "0B0C23",
                    "buyer": {
                        "first_name": "asda234",
                        "last_name": "asd",
                        "email": "dd@dd.com",
                        "username": "user111",
                        "address": {
                            "id": 5,
                            "street_address": "adasd",
                            "city": "asdad",
                            "province": "asd",
                            "zipcode": "asdasd"
                        },
                        "pk": 2
                    },
                    "date": "2021-11-01T15:53:41.150080Z",
                    "value": 13.0,
                    "billing_firstname": "asda",
                    "billing_lastname": "asd",
                    "billing_email": "dd@dd.com",
                    "billing_contact_number": "3065396709",
                    "delivered": false,
                    "pk": 4
                },
                "pk": 4
            }
        ],
        "quantity": 6
    },
    {
        "unique_order_id": "23FAF2",
        "buyer": {
            "first_name": "asda234",
            "last_name": "asd",
            "email": "dd@dd.com",
            "username": "user111",
            "address": {
                "id": 5,
                "street_address": "adasd",
                "city": "asdad",
                "province": "asd",
                "zipcode": "asdasd"
            },
            "pk": 2
        },
        "date": "2021-11-01T15:54:37.918929Z",
        "value": 12.0,
        "billing_firstname": "asda",
        "billing_lastname": "asd",
        "billing_email": "dd@dd.com",
        "billing_contact_number": "3065396709",
        "delivered": false,
        "pk": 5,
        "orderlines": [
            {
                "product": {
                    "name": "product10888",
                    "price": 1.0,
                    "quantity": 20,
                    "delivery_cost": 1.0,
                    "category": {
                        "name": "Tech",
                        "pk": 1
                    },
                    "company": {
                        "company_name": "company10",
                        "company_username": "username41",
                        "address": {
                            "id": 2,
                            "street_address": "abcd",
                            "city": "Regina",
                            "province": "sk",
                            "zipcode": "abc"
                        },
                        "pk": 1
                    },
                    "seller": {
                        "first_name": "shamsul",
                        "last_name": "arefin",
                        "email": "a@a.com",
                        "photo_id_num": null,
                        "pk": 1
                    },
                    "date": "2021-10-26T11:36:40.526778Z",
                    "pk": 4
                },
                "quantity": 1,
                "order": {
                    "unique_order_id": "23FAF2",
                    "buyer": {
                        "first_name": "asda234",
                        "last_name": "asd",
                        "email": "dd@dd.com",
                        "username": "user111",
                        "address": {
                            "id": 5,
                            "street_address": "adasd",
                            "city": "asdad",
                            "province": "asd",
                            "zipcode": "asdasd"
                        },
                        "pk": 2
                    },
                    "date": "2021-11-01T15:54:37.918929Z",
                    "value": 12.0,
                    "billing_firstname": "asda",
                    "billing_lastname": "asd",
                    "billing_email": "dd@dd.com",
                    "billing_contact_number": "3065396709",
                    "delivered": false,
                    "pk": 5
                },
                "pk": 5
            },
            {
                "product": {
                    "name": "product from the ui1",
                    "price": 1.0,
                    "quantity": 1,
                    "delivery_cost": 1.0,
                    "category": {
                        "name": "Tech",
                        "pk": 1
                    },
                    "company": {
                        "company_name": "company10",
                        "company_username": "username41",
                        "address": {
                            "id": 2,
                            "street_address": "abcd",
                            "city": "Regina",
                            "province": "sk",
                            "zipcode": "abc"
                        },
                        "pk": 1
                    },
                    "seller": {
                        "first_name": "karima",
                        "last_name": "seller",
                        "email": "b@a.com",
                        "photo_id_num": "idnum12",
                        "pk": 8
                    },
                    "date": "2021-10-27T09:04:28.130946Z",
                    "pk": 5
                },
                "quantity": 1,
                "order": {
                    "unique_order_id": "23FAF2",
                    "buyer": {
                        "first_name": "asda234",
                        "last_name": "asd",
                        "email": "dd@dd.com",
                        "username": "user111",
                        "address": {
                            "id": 5,
                            "street_address": "adasd",
                            "city": "asdad",
                            "province": "asd",
                            "zipcode": "asdasd"
                        },
                        "pk": 2
                    },
                    "date": "2021-11-01T15:54:37.918929Z",
                    "value": 12.0,
                    "billing_firstname": "asda",
                    "billing_lastname": "asd",
                    "billing_email": "dd@dd.com",
                    "billing_contact_number": "3065396709",
                    "delivered": false,
                    "pk": 5
                },
                "pk": 6
            },
            {
                "product": {
                    "name": "productui0",
                    "price": 2.0,
                    "quantity": 2,
                    "delivery_cost": 2.0,
                    "category": {
                        "name": "Tech",
                        "pk": 1
                    },
                    "company": {
                        "company_name": "company10",
                        "company_username": "username41",
                        "address": {
                            "id": 2,
                            "street_address": "abcd",
                            "city": "Regina",
                            "province": "sk",
                            "zipcode": "abc"
                        },
                        "pk": 1
                    },
                    "seller": {
                        "first_name": "karima",
                        "last_name": "seller",
                        "email": "b@a.com",
                        "photo_id_num": "idnum12",
                        "pk": 8
                    },
                    "date": "2021-10-27T09:23:29.049307Z",
                    "pk": 6
                },
                "quantity": 1,
                "order": {
                    "unique_order_id": "23FAF2",
                    "buyer": {
                        "first_name": "asda234",
                        "last_name": "asd",
                        "email": "dd@dd.com",
                        "username": "user111",
                        "address": {
                            "id": 5,
                            "street_address": "adasd",
                            "city": "asdad",
                            "province": "asd",
                            "zipcode": "asdasd"
                        },
                        "pk": 2
                    },
                    "date": "2021-11-01T15:54:37.918929Z",
                    "value": 12.0,
                    "billing_firstname": "asda",
                    "billing_lastname": "asd",
                    "billing_email": "dd@dd.com",
                    "billing_contact_number": "3065396709",
                    "delivered": false,
                    "pk": 5
                },
                "pk": 7
            },
            {
                "product": {
                    "name": "productui0",
                    "price": 2.0,
                    "quantity": 2,
                    "delivery_cost": 2.0,
                    "category": {
                        "name": "Tech",
                        "pk": 1
                    },
                    "company": {
                        "company_name": "company10",
                        "company_username": "username41",
                        "address": {
                            "id": 2,
                            "street_address": "abcd",
                            "city": "Regina",
                            "province": "sk",
                            "zipcode": "abc"
                        },
                        "pk": 1
                    },
                    "seller": {
                        "first_name": "karima",
                        "last_name": "seller",
                        "email": "b@a.com",
                        "photo_id_num": "idnum12",
                        "pk": 8
                    },
                    "date": "2021-10-27T09:23:36.470429Z",
                    "pk": 7
                },
                "quantity": 1,
                "order": {
                    "unique_order_id": "23FAF2",
                    "buyer": {
                        "first_name": "asda234",
                        "last_name": "asd",
                        "email": "dd@dd.com",
                        "username": "user111",
                        "address": {
                            "id": 5,
                            "street_address": "adasd",
                            "city": "asdad",
                            "province": "asd",
                            "zipcode": "asdasd"
                        },
                        "pk": 2
                    },
                    "date": "2021-11-01T15:54:37.918929Z",
                    "value": 12.0,
                    "billing_firstname": "asda",
                    "billing_lastname": "asd",
                    "billing_email": "dd@dd.com",
                    "billing_contact_number": "3065396709",
                    "delivered": false,
                    "pk": 5
                },
                "pk": 8
            }
        ],
        "quantity": 4
    },
    {
        "unique_order_id": "CBB989",
        "buyer": {
            "first_name": "asda234",
            "last_name": "asd",
            "email": "dd@dd.com",
            "username": "user111",
            "address": {
                "id": 5,
                "street_address": "adasd",
                "city": "asdad",
                "province": "asd",
                "zipcode": "asdasd"
            },
            "pk": 2
        },
        "date": "2021-11-01T16:28:27.813938Z",
        "value": 6.0,
        "billing_firstname": "asda",
        "billing_lastname": "asd",
        "billing_email": "dd@dd.com",
        "billing_contact_number": "45455",
        "delivered": false,
        "pk": 6,
        "orderlines": [
            {
                "product": {
                    "name": "productui0",
                    "price": 2.0,
                    "quantity": 2,
                    "delivery_cost": 2.0,
                    "category": {
                        "name": "Tech",
                        "pk": 1
                    },
                    "company": {
                        "company_name": "company10",
                        "company_username": "username41",
                        "address": {
                            "id": 2,
                            "street_address": "abcd",
                            "city": "Regina",
                            "province": "sk",
                            "zipcode": "abc"
                        },
                        "pk": 1
                    },
                    "seller": {
                        "first_name": "karima",
                        "last_name": "seller",
                        "email": "b@a.com",
                        "photo_id_num": "idnum12",
                        "pk": 8
                    },
                    "date": "2021-10-27T09:23:29.049307Z",
                    "pk": 6
                },
                "quantity": 1,
                "order": {
                    "unique_order_id": "CBB989",
                    "buyer": {
                        "first_name": "asda234",
                        "last_name": "asd",
                        "email": "dd@dd.com",
                        "username": "user111",
                        "address": {
                            "id": 5,
                            "street_address": "adasd",
                            "city": "asdad",
                            "province": "asd",
                            "zipcode": "asdasd"
                        },
                        "pk": 2
                    },
                    "date": "2021-11-01T16:28:27.813938Z",
                    "value": 6.0,
                    "billing_firstname": "asda",
                    "billing_lastname": "asd",
                    "billing_email": "dd@dd.com",
                    "billing_contact_number": "45455",
                    "delivered": false,
                    "pk": 6
                },
                "pk": 10
            }
        ],
        "quantity": 1
    },
    {
        "unique_order_id": "E57791",
        "buyer": {
            "first_name": "asda234",
            "last_name": "asd",
            "email": "dd@dd.com",
            "username": "user111",
            "address": {
                "id": 5,
                "street_address": "adasd",
                "city": "asdad",
                "province": "asd",
                "zipcode": "asdasd"
            },
            "pk": 2
        },
        "date": "2021-11-01T16:29:10.959364Z",
        "value": 4.0,
        "billing_firstname": "asda",
        "billing_lastname": "asd",
        "billing_email": "dd@dd.com",
        "billing_contact_number": "45454",
        "delivered": false,
        "pk": 7,
        "orderlines": [
            {
                "product": {
                    "name": "product10888",
                    "price": 1.0,
                    "quantity": 20,
                    "delivery_cost": 1.0,
                    "category": {
                        "name": "Tech",
                        "pk": 1
                    },
                    "company": {
                        "company_name": "company10",
                        "company_username": "username41",
                        "address": {
                            "id": 2,
                            "street_address": "abcd",
                            "city": "Regina",
                            "province": "sk",
                            "zipcode": "abc"
                        },
                        "pk": 1
                    },
                    "seller": {
                        "first_name": "shamsul",
                        "last_name": "arefin",
                        "email": "a@a.com",
                        "photo_id_num": null,
                        "pk": 1
                    },
                    "date": "2021-10-26T11:36:40.526778Z",
                    "pk": 4
                },
                "quantity": 1,
                "order": {
                    "unique_order_id": "E57791",
                    "buyer": {
                        "first_name": "asda234",
                        "last_name": "asd",
                        "email": "dd@dd.com",
                        "username": "user111",
                        "address": {
                            "id": 5,
                            "street_address": "adasd",
                            "city": "asdad",
                            "province": "asd",
                            "zipcode": "asdasd"
                        },
                        "pk": 2
                    },
                    "date": "2021-11-01T16:29:10.959364Z",
                    "value": 4.0,
                    "billing_firstname": "asda",
                    "billing_lastname": "asd",
                    "billing_email": "dd@dd.com",
                    "billing_contact_number": "45454",
                    "delivered": false,
                    "pk": 7
                },
                "pk": 11
            },
            {
                "product": {
                    "name": "product from the ui1",
                    "price": 1.0,
                    "quantity": 1,
                    "delivery_cost": 1.0,
                    "category": {
                        "name": "Tech",
                        "pk": 1
                    },
                    "company": {
                        "company_name": "company10",
                        "company_username": "username41",
                        "address": {
                            "id": 2,
                            "street_address": "abcd",
                            "city": "Regina",
                            "province": "sk",
                            "zipcode": "abc"
                        },
                        "pk": 1
                    },
                    "seller": {
                        "first_name": "karima",
                        "last_name": "seller",
                        "email": "b@a.com",
                        "photo_id_num": "idnum12",
                        "pk": 8
                    },
                    "date": "2021-10-27T09:04:28.130946Z",
                    "pk": 5
                },
                "quantity": 1,
                "order": {
                    "unique_order_id": "E57791",
                    "buyer": {
                        "first_name": "asda234",
                        "last_name": "asd",
                        "email": "dd@dd.com",
                        "username": "user111",
                        "address": {
                            "id": 5,
                            "street_address": "adasd",
                            "city": "asdad",
                            "province": "asd",
                            "zipcode": "asdasd"
                        },
                        "pk": 2
                    },
                    "date": "2021-11-01T16:29:10.959364Z",
                    "value": 4.0,
                    "billing_firstname": "asda",
                    "billing_lastname": "asd",
                    "billing_email": "dd@dd.com",
                    "billing_contact_number": "45454",
                    "delivered": false,
                    "pk": 7
                },
                "pk": 12
            }
        ],
        "quantity": 2
    },
    {
        "unique_order_id": "BEAD47",
        "buyer": {
            "first_name": "asda234",
            "last_name": "asd",
            "email": "dd@dd.com",
            "username": "user111",
            "address": {
                "id": 5,
                "street_address": "adasd",
                "city": "asdad",
                "province": "asd",
                "zipcode": "asdasd"
            },
            "pk": 2
        },
        "date": "2021-11-01T16:29:55.400363Z",
        "value": 9.0,
        "billing_firstname": "asda",
        "billing_lastname": "asd",
        "billing_email": "dd@dd.com",
        "billing_contact_number": "454545",
        "delivered": false,
        "pk": 8,
        "orderlines": [
            {
                "product": {
                    "name": "product10888",
                    "price": 1.0,
                    "quantity": 20,
                    "delivery_cost": 1.0,
                    "category": {
                        "name": "Tech",
                        "pk": 1
                    },
                    "company": {
                        "company_name": "company10",
                        "company_username": "username41",
                        "address": {
                            "id": 2,
                            "street_address": "abcd",
                            "city": "Regina",
                            "province": "sk",
                            "zipcode": "abc"
                        },
                        "pk": 1
                    },
                    "seller": {
                        "first_name": "shamsul",
                        "last_name": "arefin",
                        "email": "a@a.com",
                        "photo_id_num": null,
                        "pk": 1
                    },
                    "date": "2021-10-26T11:36:40.526778Z",
                    "pk": 4
                },
                "quantity": 6,
                "order": {
                    "unique_order_id": "BEAD47",
                    "buyer": {
                        "first_name": "asda234",
                        "last_name": "asd",
                        "email": "dd@dd.com",
                        "username": "user111",
                        "address": {
                            "id": 5,
                            "street_address": "adasd",
                            "city": "asdad",
                            "province": "asd",
                            "zipcode": "asdasd"
                        },
                        "pk": 2
                    },
                    "date": "2021-11-01T16:29:55.400363Z",
                    "value": 9.0,
                    "billing_firstname": "asda",
                    "billing_lastname": "asd",
                    "billing_email": "dd@dd.com",
                    "billing_contact_number": "454545",
                    "delivered": false,
                    "pk": 8
                },
                "pk": 13
            },
            {
                "product": {
                    "name": "product from the ui1",
                    "price": 1.0,
                    "quantity": 1,
                    "delivery_cost": 1.0,
                    "category": {
                        "name": "Tech",
                        "pk": 1
                    },
                    "company": {
                        "company_name": "company10",
                        "company_username": "username41",
                        "address": {
                            "id": 2,
                            "street_address": "abcd",
                            "city": "Regina",
                            "province": "sk",
                            "zipcode": "abc"
                        },
                        "pk": 1
                    },
                    "seller": {
                        "first_name": "karima",
                        "last_name": "seller",
                        "email": "b@a.com",
                        "photo_id_num": "idnum12",
                        "pk": 8
                    },
                    "date": "2021-10-27T09:04:28.130946Z",
                    "pk": 5
                },
                "quantity": 1,
                "order": {
                    "unique_order_id": "BEAD47",
                    "buyer": {
                        "first_name": "asda234",
                        "last_name": "asd",
                        "email": "dd@dd.com",
                        "username": "user111",
                        "address": {
                            "id": 5,
                            "street_address": "adasd",
                            "city": "asdad",
                            "province": "asd",
                            "zipcode": "asdasd"
                        },
                        "pk": 2
                    },
                    "date": "2021-11-01T16:29:55.400363Z",
                    "value": 9.0,
                    "billing_firstname": "asda",
                    "billing_lastname": "asd",
                    "billing_email": "dd@dd.com",
                    "billing_contact_number": "454545",
                    "delivered": false,
                    "pk": 8
                },
                "pk": 14
            }
        ],
        "quantity": 7
    },
    {
        "unique_order_id": "5127C5",
        "buyer": {
            "first_name": "asda234",
            "last_name": "asd",
            "email": "dd@dd.com",
            "username": "user111",
            "address": {
                "id": 5,
                "street_address": "adasd",
                "city": "asdad",
                "province": "asd",
                "zipcode": "asdasd"
            },
            "pk": 2
        },
        "date": "2021-11-01T19:44:31.773696Z",
        "value": 34.0,
        "billing_firstname": "asda",
        "billing_lastname": "asd",
        "billing_email": "dd@dd.com",
        "billing_contact_number": "554545",
        "delivered": false,
        "pk": 9,
        "orderlines": [
            {
                "product": {
                    "name": "product10888",
                    "price": 1.0,
                    "quantity": 20,
                    "delivery_cost": 1.0,
                    "category": {
                        "name": "Tech",
                        "pk": 1
                    },
                    "company": {
                        "company_name": "company10",
                        "company_username": "username41",
                        "address": {
                            "id": 2,
                            "street_address": "abcd",
                            "city": "Regina",
                            "province": "sk",
                            "zipcode": "abc"
                        },
                        "pk": 1
                    },
                    "seller": {
                        "first_name": "shamsul",
                        "last_name": "arefin",
                        "email": "a@a.com",
                        "photo_id_num": null,
                        "pk": 1
                    },
                    "date": "2021-10-26T11:36:40.526778Z",
                    "pk": 4
                },
                "quantity": 1,
                "order": {
                    "unique_order_id": "5127C5",
                    "buyer": {
                        "first_name": "asda234",
                        "last_name": "asd",
                        "email": "dd@dd.com",
                        "username": "user111",
                        "address": {
                            "id": 5,
                            "street_address": "adasd",
                            "city": "asdad",
                            "province": "asd",
                            "zipcode": "asdasd"
                        },
                        "pk": 2
                    },
                    "date": "2021-11-01T19:44:31.773696Z",
                    "value": 34.0,
                    "billing_firstname": "asda",
                    "billing_lastname": "asd",
                    "billing_email": "dd@dd.com",
                    "billing_contact_number": "554545",
                    "delivered": false,
                    "pk": 9
                },
                "pk": 16
            },
            {
                "product": {
                    "name": "product from the ui1",
                    "price": 1.0,
                    "quantity": 1,
                    "delivery_cost": 1.0,
                    "category": {
                        "name": "Tech",
                        "pk": 1
                    },
                    "company": {
                        "company_name": "company10",
                        "company_username": "username41",
                        "address": {
                            "id": 2,
                            "street_address": "abcd",
                            "city": "Regina",
                            "province": "sk",
                            "zipcode": "abc"
                        },
                        "pk": 1
                    },
                    "seller": {
                        "first_name": "karima",
                        "last_name": "seller",
                        "email": "b@a.com",
                        "photo_id_num": "idnum12",
                        "pk": 8
                    },
                    "date": "2021-10-27T09:04:28.130946Z",
                    "pk": 5
                },
                "quantity": 1,
                "order": {
                    "unique_order_id": "5127C5",
                    "buyer": {
                        "first_name": "asda234",
                        "last_name": "asd",
                        "email": "dd@dd.com",
                        "username": "user111",
                        "address": {
                            "id": 5,
                            "street_address": "adasd",
                            "city": "asdad",
                            "province": "asd",
                            "zipcode": "asdasd"
                        },
                        "pk": 2
                    },
                    "date": "2021-11-01T19:44:31.773696Z",
                    "value": 34.0,
                    "billing_firstname": "asda",
                    "billing_lastname": "asd",
                    "billing_email": "dd@dd.com",
                    "billing_contact_number": "554545",
                    "delivered": false,
                    "pk": 9
                },
                "pk": 17
            },
            {
                "product": {
                    "name": "productui0",
                    "price": 2.0,
                    "quantity": 2,
                    "delivery_cost": 2.0,
                    "category": {
                        "name": "Tech",
                        "pk": 1
                    },
                    "company": {
                        "company_name": "company10",
                        "company_username": "username41",
                        "address": {
                            "id": 2,
                            "street_address": "abcd",
                            "city": "Regina",
                            "province": "sk",
                            "zipcode": "abc"
                        },
                        "pk": 1
                    },
                    "seller": {
                        "first_name": "karima",
                        "last_name": "seller",
                        "email": "b@a.com",
                        "photo_id_num": "idnum12",
                        "pk": 8
                    },
                    "date": "2021-10-27T09:23:29.049307Z",
                    "pk": 6
                },
                "quantity": 2,
                "order": {
                    "unique_order_id": "5127C5",
                    "buyer": {
                        "first_name": "asda234",
                        "last_name": "asd",
                        "email": "dd@dd.com",
                        "username": "user111",
                        "address": {
                            "id": 5,
                            "street_address": "adasd",
                            "city": "asdad",
                            "province": "asd",
                            "zipcode": "asdasd"
                        },
                        "pk": 2
                    },
                    "date": "2021-11-01T19:44:31.773696Z",
                    "value": 34.0,
                    "billing_firstname": "asda",
                    "billing_lastname": "asd",
                    "billing_email": "dd@dd.com",
                    "billing_contact_number": "554545",
                    "delivered": false,
                    "pk": 9
                },
                "pk": 18
            },
            {
                "product": {
                    "name": "productui0",
                    "price": 2.0,
                    "quantity": 2,
                    "delivery_cost": 2.0,
                    "category": {
                        "name": "Tech",
                        "pk": 1
                    },
                    "company": {
                        "company_name": "company10",
                        "company_username": "username41",
                        "address": {
                            "id": 2,
                            "street_address": "abcd",
                            "city": "Regina",
                            "province": "sk",
                            "zipcode": "abc"
                        },
                        "pk": 1
                    },
                    "seller": {
                        "first_name": "karima",
                        "last_name": "seller",
                        "email": "b@a.com",
                        "photo_id_num": "idnum12",
                        "pk": 8
                    },
                    "date": "2021-10-27T09:23:50.846307Z",
                    "pk": 10
                },
                "quantity": 1,
                "order": {
                    "unique_order_id": "5127C5",
                    "buyer": {
                        "first_name": "asda234",
                        "last_name": "asd",
                        "email": "dd@dd.com",
                        "username": "user111",
                        "address": {
                            "id": 5,
                            "street_address": "adasd",
                            "city": "asdad",
                            "province": "asd",
                            "zipcode": "asdasd"
                        },
                        "pk": 2
                    },
                    "date": "2021-11-01T19:44:31.773696Z",
                    "value": 34.0,
                    "billing_firstname": "asda",
                    "billing_lastname": "asd",
                    "billing_email": "dd@dd.com",
                    "billing_contact_number": "554545",
                    "delivered": false,
                    "pk": 9
                },
                "pk": 19
            },
            {
                "product": {
                    "name": "productui0",
                    "price": 2.0,
                    "quantity": 2,
                    "delivery_cost": 2.0,
                    "category": {
                        "name": "Tech",
                        "pk": 1
                    },
                    "company": {
                        "company_name": "company10",
                        "company_username": "username41",
                        "address": {
                            "id": 2,
                            "street_address": "abcd",
                            "city": "Regina",
                            "province": "sk",
                            "zipcode": "abc"
                        },
                        "pk": 1
                    },
                    "seller": {
                        "first_name": "karima",
                        "last_name": "seller",
                        "email": "b@a.com",
                        "photo_id_num": "idnum12",
                        "pk": 8
                    },
                    "date": "2021-10-27T09:23:36.470429Z",
                    "pk": 7
                },
                "quantity": 2,
                "order": {
                    "unique_order_id": "5127C5",
                    "buyer": {
                        "first_name": "asda234",
                        "last_name": "asd",
                        "email": "dd@dd.com",
                        "username": "user111",
                        "address": {
                            "id": 5,
                            "street_address": "adasd",
                            "city": "asdad",
                            "province": "asd",
                            "zipcode": "asdasd"
                        },
                        "pk": 2
                    },
                    "date": "2021-11-01T19:44:31.773696Z",
                    "value": 34.0,
                    "billing_firstname": "asda",
                    "billing_lastname": "asd",
                    "billing_email": "dd@dd.com",
                    "billing_contact_number": "554545",
                    "delivered": false,
                    "pk": 9
                },
                "pk": 20
            },
            {
                "product": {
                    "name": "productui0",
                    "price": 2.0,
                    "quantity": 2,
                    "delivery_cost": 2.0,
                    "category": {
                        "name": "Tech",
                        "pk": 1
                    },
                    "company": {
                        "company_name": "company10",
                        "company_username": "username41",
                        "address": {
                            "id": 2,
                            "street_address": "abcd",
                            "city": "Regina",
                            "province": "sk",
                            "zipcode": "abc"
                        },
                        "pk": 1
                    },
                    "seller": {
                        "first_name": "karima",
                        "last_name": "seller",
                        "email": "b@a.com",
                        "photo_id_num": "idnum12",
                        "pk": 8
                    },
                    "date": "2021-10-27T09:23:49.094448Z",
                    "pk": 8
                },
                "quantity": 1,
                "order": {
                    "unique_order_id": "5127C5",
                    "buyer": {
                        "first_name": "asda234",
                        "last_name": "asd",
                        "email": "dd@dd.com",
                        "username": "user111",
                        "address": {
                            "id": 5,
                            "street_address": "adasd",
                            "city": "asdad",
                            "province": "asd",
                            "zipcode": "asdasd"
                        },
                        "pk": 2
                    },
                    "date": "2021-11-01T19:44:31.773696Z",
                    "value": 34.0,
                    "billing_firstname": "asda",
                    "billing_lastname": "asd",
                    "billing_email": "dd@dd.com",
                    "billing_contact_number": "554545",
                    "delivered": false,
                    "pk": 9
                },
                "pk": 21
            },
            {
                "product": {
                    "name": "productui0",
                    "price": 2.0,
                    "quantity": 2,
                    "delivery_cost": 2.0,
                    "category": {
                        "name": "Tech",
                        "pk": 1
                    },
                    "company": {
                        "company_name": "company10",
                        "company_username": "username41",
                        "address": {
                            "id": 2,
                            "street_address": "abcd",
                            "city": "Regina",
                            "province": "sk",
                            "zipcode": "abc"
                        },
                        "pk": 1
                    },
                    "seller": {
                        "first_name": "karima",
                        "last_name": "seller",
                        "email": "b@a.com",
                        "photo_id_num": "idnum12",
                        "pk": 8
                    },
                    "date": "2021-10-27T09:24:56.036450Z",
                    "pk": 12
                },
                "quantity": 1,
                "order": {
                    "unique_order_id": "5127C5",
                    "buyer": {
                        "first_name": "asda234",
                        "last_name": "asd",
                        "email": "dd@dd.com",
                        "username": "user111",
                        "address": {
                            "id": 5,
                            "street_address": "adasd",
                            "city": "asdad",
                            "province": "asd",
                            "zipcode": "asdasd"
                        },
                        "pk": 2
                    },
                    "date": "2021-11-01T19:44:31.773696Z",
                    "value": 34.0,
                    "billing_firstname": "asda",
                    "billing_lastname": "asd",
                    "billing_email": "dd@dd.com",
                    "billing_contact_number": "554545",
                    "delivered": false,
                    "pk": 9
                },
                "pk": 22
            },
            {
                "product": {
                    "name": "productui0",
                    "price": 2.0,
                    "quantity": 2,
                    "delivery_cost": 2.0,
                    "category": {
                        "name": "Tech",
                        "pk": 1
                    },
                    "company": {
                        "company_name": "company10",
                        "company_username": "username41",
                        "address": {
                            "id": 2,
                            "street_address": "abcd",
                            "city": "Regina",
                            "province": "sk",
                            "zipcode": "abc"
                        },
                        "pk": 1
                    },
                    "seller": {
                        "first_name": "karima",
                        "last_name": "seller",
                        "email": "b@a.com",
                        "photo_id_num": "idnum12",
                        "pk": 8
                    },
                    "date": "2021-10-27T09:23:50.575506Z",
                    "pk": 9
                },
                "quantity": 1,
                "order": {
                    "unique_order_id": "5127C5",
                    "buyer": {
                        "first_name": "asda234",
                        "last_name": "asd",
                        "email": "dd@dd.com",
                        "username": "user111",
                        "address": {
                            "id": 5,
                            "street_address": "adasd",
                            "city": "asdad",
                            "province": "asd",
                            "zipcode": "asdasd"
                        },
                        "pk": 2
                    },
                    "date": "2021-11-01T19:44:31.773696Z",
                    "value": 34.0,
                    "billing_firstname": "asda",
                    "billing_lastname": "asd",
                    "billing_email": "dd@dd.com",
                    "billing_contact_number": "554545",
                    "delivered": false,
                    "pk": 9
                },
                "pk": 23
            }
        ],
        "quantity": 10
    }
]
```

- Order detail with the orderlines: same as above
- Login Authentication response:
```
{
    "token": "76f4b4691397991c2d1b62f9c706612fff655a77",
    "buyer": {
        "first_name": "karima",
        "last_name": "khan",
        "email": "karima@12.com",
        "username": "12312",
        "address": null,
        "pk": 10
    }
}
for the seller user the seller details will be returned with the key seller
```

## Tutorial to use the APIs
# How to add a product (as a seller)
- First register as a seller user
- Then login as a seller
- Then add a category (if not existed)
- Then add a company (if not existed)
- Add a product specifying product details, category_id,seller_id,company_id

# How to add product to cart
- First register as a buyer and login
- create a cart with the buyer (a buyer can have only one cart)
- call add product to cart API specifying cart_id, product_id

# How to order
- Register as a buyer and login
- add product(s) to the cart
- call order create api, it will automatically move the cart items to a new order, create orderlines under the order

# How to get the all the orders of someone
- Call the orderlist with orderlines of a user api

# How to get all the cart items of a user
- Call the cart with cartlines by user API
