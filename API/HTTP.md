
# HTTP

- when the client sends the message to the server using http, we refer the msg as “Http request” and the response that is sent by server is called “Http response.”


## HTTP Request Message

The request message contains the following parts:

- **URL** (e.g., `https://www.facebook.com`)
- **Request Method** (e.g., `POST`)
- **Headers** (e.g., `User-Agent: iPhone`)
- **Body** (e.g., `"message": "I’m learning about HTTP!"`)


### URL (Uniform Resource Locator)

- A web address.
- URLs are used to locate web pages.
- A resource (like a web page) contains information; the URL helps locate that resource.
- URLs can be used from any location on Earth to access the same resource over the internet.

### Example  
Address pointing to the latest US National Public Radio (NPR) news:
`https://www.npr.org/sections/news`

- **https:** → Communication protocol  
- **www.npr.org:** → Domain name  
- **sections/news:** → Path  

---

### Request Method

The request method indicates the intention of the client.

#### **GET**
Used to retrieve existing data.

Examples:  
1. When browsing the internet, the browser sends GET requests to fetch the latest information.  
2. When checking an order list, data is retrieved from the server.

#### **POST**
- Used to create a new database.
- If the ID matches with the existing database it would update the entry with that ID.

Example:  
- Adding items to a cart or placing an order — this information is posted to the server.

#### **PUT**
- Used to edit or update existing data.
- The **PUT** method is used for modifying an existing resource.  
- When using PUT, the client must send **all the data** required to update the entire resource — not just the part that changed.

### Example
- If we want to update only the car name, model, or year, we **cannot** send just the year or just the model.  
We must send the **entire updated data object** representing the resource.
- Replacing an existing item in an order while keeping the same order ID.

### Important Point
To update a resource using PUT, the **correct ID** of the resource must be provided.


#### **DELETE**
Used to delete data.

Example:  
- Removing an item from the ordered list.

## GET vs POST

| GET | POST |
|-----|------|
| Used for getting data | Used for creating data |
| Parameters are in the URL | Parameters can be in both URL and body |
| Does not have a request body | The request body contains the data we want to create |

---

## POST vs PUT

| POST | PUT |
|------|-----|
| Used for creating data. May also update data in some cases. | Used for updating data. |
| Parameters can be in both URL and body. | Parameters can be in both URL and body. |
| The request body contains the data we want to create. | The request body contains the data we want to update. |
| Never cached. | Never cached. |
| No identifier required. | Identifier is mandatory. |

### HTTP Methods and Endpoints

| HTTP Method | Endpoint                  | Meaning                              |
|-------------|----------------------------|----------------------------------------|
| GET         | /orders                    | Get all orders from all customers     |
| POST        | /orders                    | Create a new order                    |
| GET         | /orders/2356               | Get order #2356                       |
| DELETE      | /orders/2356               | Cancel order #2356                    |
| GET         | /customers/1234/orders     | Get all orders for customer #1234     |

### Headers

- Provide meta-information (information about other information).  
- Not always required.  
- Similar to barcodes on packages — they help identify and process requests.
- we can see some auto generated headers

---

### Body

- Contains data the client wants to send to the server.  
- **GET** requests do **not** include a body.  
- **POST** requests usually include one.

Example:  
- When posting a Facebook status, the body contains the actual message.

---

## HTTP Response Message

A response message contains:

- **Status Code** (e.g., `200`, `404`)  
- **Headers** (e.g., `content-type: text/html`)  
- **Body** (e.g., `<html><title>latest news</title></html>`)

---

### Status Code

- A three-digit code indicating processing status.  
- `200` → Request successful  
- `404` → Requested page/resource not found  

---

### Headers

- Headers are also present in the response and provide additional information about the response.  
- If the server wants to tell the client that the response is in HTML, it will include a header such as:  
  `content-type: text/html`  
- Headers can also indicate formats like JSON, XML, etc.
- we can see some auto generated headers.

### Body

- The body contains the data the server wants to send to the client.  
- Example: Like the body of a letter, it holds the main content.

## CRUD

- **Create** — `POST`
- **Read/Retrieve** — `GET`
- **Update** — `PUT`, `POST`, `PATCH`
- **Delete** — `DELETE`
