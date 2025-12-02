## Status Code

- A quick way to determine whether a request was successful without inspecting the response body.  
- Simplifies error handling on the client side.  
- There are **5 groups** of HTTP status codes:

---

### **2xx – Successful**
Examples: `200 OK`, `201 Created`  
- The request was **received**, **understood**, and **accepted**.

---

### **4xx – Client Errors**
Examples: `400 Bad Request`, `401 Unauthorized`, `403 Forbidden`, `404 Not Found`  
- The request was **received** and **understood**, but **rejected** due to an issue caused by the client.

---

### **5xx – Server Errors**
Examples: `500 Internal Server Error`, `503 Service Unavailable`  
- The request was received, but the server **failed to process** it due to an internal error.

---

### **1xx – Informational**
- The request was received and understood, but processing has **not finished yet**.

---

### **3xx – Redirection**
Example: `301 Moved Permanently`  
- The request was received and understood, but the requested information has **moved** or is available at a different location.

---

### Note
- If the server is **down**, there is **no status code**, because no one is available to generate it.
