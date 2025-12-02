# REST

REST stands for **Representational State Transfer** and defines a set of rules and principles used when building APIs.

- It is an **architectural style** for building APIs (not a protocol or standard).
- REST defines a set of **architectural constraints**, but there is no official standard.
- **RESTful Web Services** refers to the same concept as REST.

---

## Resource

A **resource** is any information that can be named.

Examples of resources include:

- Documents  
- Weather in New York  
- Representation of a real-world object  
- A collection of resources  

Common resource examples:

- **Person** → name, email, address, age  
- **Purchase Order** → product ID, seller details, buyer details  
- **Student Grades** → different grade values for different subjects  

### Example: Pizzeria API

**Customer-facing resources**
- Menu  
- Pizza (size, crust)  
- Topping  
- Sauce  

**Business-facing resources**
- Order  
- Customer  
- Address  
- Payment  

---

## Resource Identifiers

To access a resource, it must have a **resource identifier**, usually a **URL**.

Examples:

- `http://example.com/orders`
- `http://example.com/orders/93246`  
  - `93246` → unique identifier
- `http://example.com/customers/82762/orders`  
  - `customers/82762/orders` → endpoint for customer-specific orders

---

# JSON (JavaScript Object Notation)

- **JavaScript** → programming language  
- **Object** → contains data  
- **Notation** → rules to represent something  

JSON characteristics:

- Free to use (no license required)
- Must follow strict formatting rules
- Uses **key–value pairs**
  - Keys must be strings  
  - Values can be strings, numbers, arrays, objects, etc.  
- Strings must be wrapped in **double quotes ("")**
- Every opening `{` must have a closing `}`  
- The last key-value pair **should not** end with a comma  

### Example JSON

the entire example is an object of a person

```json
{
  "name": "manaswini"
}
{
  "FirstName": "Chenna",
  "age": 25,
  "hobbies": ["Netflix", "music"],
  "contactdetails": {
    "phone": "23423",
    "email": "chenna@example.com"
    }
}
```

# Serialization & Deserialization

Python Program → serialization → JSON → deserialization → PHP Program

## If invalid JSON is provided:

- You may still see a “body” in the response
- The API will likely return an error (e.g., null)
- Tools may highlight invalid sections

## Swagger

Swagger is used to describe the structure of APIs. An API specification is a way to define REST APIs, and it includes:

- Available endpoints  
- Operations (GET, POST, PUT, ...)  
- Input and output parameters  

## Swagger UI

Swagger UI renders the Swagger specification (stored in **JSON** or **YAML**) into interactive API documentation.  
It has now become an official specification called **OpenAPI**.
