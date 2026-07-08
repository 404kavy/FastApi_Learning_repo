# 🏥 Patient Management System API

Welcome to the **Patient Management System API**! This repository is a comprehensive, beginner-to-intermediate guide to building RESTful APIs using **FastAPI** and **Pydantic**. 

Whether you are writing your first line of backend code or looking to solidify your understanding of data validation and serialization, this project is designed to teach you everything from scratch.

---

## 1. Project Overview

### What does this project do?
This project is a fully functional REST API that manages patient medical records. It allows users to create, read, update, and delete (CRUD) patient data. It also automatically calculates Body Mass Index (BMI) and provides a health verdict based on the patient's height and weight.

### What problem does it solve?
Managing patient records manually (e.g., in spreadsheets) is error-prone, lacks data validation (e.g., negative weights, invalid emails), and is hard to integrate with other systems. This API solves that by providing a structured, validated, and automated digital system.

### Why was this project built?
To serve as an educational blueprint. It bridges the gap between basic Python scripting and production-ready backend development, showcasing advanced Pydantic validation, data serialization, and FastAPI routing.

### Technologies Used
- **Python 3.10+**: The core programming language.
- **FastAPI**: A modern, high-performance web framework for building APIs.
- **Pydantic**: Data validation using Python type annotations.
- **JSON**: The lightweight data-interchange format used for storage.
- **Uvicorn**: An ASGI web server implementation for Python.

---

## 2. Folder Structure
