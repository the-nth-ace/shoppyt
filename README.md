# 🛍️ Shoppyt

## 🌎  Scope of the project

**What Shoppyt is:** I developed *Shoppyt* in order for me to continue to familiarize myself with FastAPI, and to go beyond developing APIs with *simple* CRUD endpoints. It is an E-Commerce API that allows multiple Vendors(Sellers) to post their Products for Buyers to purchase. Furthermore, it is my first time working with GraphQL, so this project is a differnt way to approach a familar problem. It proposes to includes multiple payment options: *Stripe* for international transactions, and *Paystack* and *Kuda API* for local transactions.

**What Shoppy isn’t:** *Shoppyt* is far from a production ready API, and the test coverage is not complete. Some features may also not scale.

## 🚂 Tech Stack

- 💨 FastAPI - A modern asynchronous batteries included Python web framework
- 📈 NeoJ4

## 📦 Proposed Features

- 🛒 User Carts
- 🏪 Vendor Listings
- 🥇 App wide best sellers
- 💳 Checkout with Stripe, Paystack and Kuda.

## 🗺️ Architectural Consideration

### Architecture

Shoppyt follows a 3-Tier Architecture of

- Controller
- Services
- Repository

Which is inspired by NestJS’s architecture. 

### Dependency Injection

I will be using the [Dependency Injector](https://python-dependency-injector.ets-labs.org/introduction/index.html) along with FastAPI’s own Dependency injector in other achieve the three layered architecture.