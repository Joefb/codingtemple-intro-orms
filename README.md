## **Overview**

This homework assignment will test your understanding of database relationships and SQLAlchemy ORM. You'll build a **Pet Clinic Management System** that demonstrates both association tables and association models.

---

## **Learning Objectives**

By completing this homework, you will:

* Implement many-to-many relationships using either Table objects or declarative models  
* Manage database sessions and transactions effectively  
* Use modern SQLAlchemy 2.0 syntax with Mapped and mapped\_column

---

## **Assignment: Pet Clinic Management System**

### **Part 1: Database Design**

Create a simplified pet clinic management system with the following entities:

#### **Core Models:**

1. **Pet** \- Contains pet information (name, species, breed, age)  
2. **Owner** \- Contains pet owner information (name, phone, email)  
3. **Veterinarian** \- Contains veterinarian information (name, specialization)  
4. **Appointment** \- Contains appointment information (date, notes, status)

#### **Relationships:**

* **Pets ↔ Owners**: Many-to-one (multiple pets can belong to one owner)  
* **Pets ↔ Veterinarians**: Many-to-many (pets can see multiple vets, vets can treat multiple pets)  
* **Appointments**: Connect pets, veterinarians, and appointment details (Junction Table between Pet and Vet)

**Set Up**

```shell
windows
python -m venv venv
venv\Scripts\activate

mac
python3 -m venv venv
source venv/bin/activate

pip install sqlalchemy

pip freeze > requirements.txt
```

### **Part 2: Implementation Requirements**

#### **2.1 Model Definitions**

Create the following models using modern SQLAlchemy 2.0 syntax:

```py
# Required imports
from sqlalchemy import create_engine, Integer, String, ForeignKey, DateTime, Table, Column
from sqlalchemy.orm import declarative_base, relationship, sessionmaker, Mapped, mapped_column
from datetime import datetime

engine = create_engine('sqlite:///clinic.db')

Session = sessionmaker(bind=engine)
session = Session() #Create Sessions


Base.metadata.create_all(bind=engine) #Add to the bottom of page

```

**Models to implement:**

1. **Owner Model** with:  
   * id (primary key)  
   * name (string, not null)  
   * phone (string, not null)  
   * email (string, unique)  
   * Relationship to pets  
2. **Pet Model** with:  
   * id (primary key)  
   * name (string, not null)  
   * species (string, not null) \- e.g., "Dog", "Cat", "Bird"  
   * breed (string)  
   * age (integer)  
   * owner\_id (foreign key to owners)  
   * Relationships to owner, veterinarians, and appointments (if you do the association model)  
3. **Veterinarian Model** with:  
   * id (primary key)  
   * name (string, not null)  
   * specialization (string) \- e.g., "General", "Surgery", "Dermatology"  
   * email (string, unique)  
   * Relationships to pets and appointments (if you do the association model)  
4. **Appointment Junction Table** :  
   Either Simple **Table object** connecting Pet and Vet ids  
   **or** Association Model with the following fields  
   * id (primary key)  
   * pet\_id (foreign key to pets)  
   * veterinarian\_id (foreign key to veterinarians)  
   * appointment\_date (datetime, not null)  
   * notes (text)  
   * status (string, default "Scheduled") \- "Scheduled", "Completed", "Cancelled"  
   * Relationships to pet and veterinarian

#### **2.3 Database Setup**

Create a function to:

* Set up the database engine  
* Create all tables  
* Return a session factory

### **Part 3: Database Population**

Add sample data to your database using SQLAlchemy session operations. You should create your own data and add it to the database.

**Requirements:**

* Add at least 3 owners with different contact information  
* Add at least 6 pets (mix of dogs, cats, birds) belonging to different owners  
* Add at least 2 veterinarians with different specializations  
* Create appointments connecting pets and veterinarians  
* Demonstrate both many-to-one and many-to-many relationships

**Tips:**

* Use session.add() for individual objects or session.add\_all() for multiple objects  
* Remember to call session.commit() to save your changes  
* Make sure your relationships are properly set up before adding data

