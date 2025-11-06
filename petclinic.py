# Required imports
from sqlalchemy import (
    create_engine,
    Integer,
    String,
    ForeignKey,
    Table,
    Column,
)
from sqlalchemy.orm import (
    declarative_base,
    relationship,
    sessionmaker,
    Mapped,
    mapped_column,
)

# Create engine
engine = create_engine("sqlite:///clinic.db", echo=True)
# Create Base instance
Base = declarative_base()

appointment = Table(
    "appointments",
    Base.metadata,
    Column("vet_id", Integer, ForeignKey("vets.id")),
    Column("pet_id", Integer, ForeignKey("pets.id")),
)


class Owner(Base):
    __tablename__ = "owners"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    phone: Mapped[str] = mapped_column(String(25), nullable=False)
    email: Mapped[str] = mapped_column(String(150), unique=True)
    # Set pointer to owner attribute in Pet
    pets: Mapped[list["Pet"]] = relationship("Pet", back_populates="owner")


class Pet(Base):
    __tablename__ = "pets"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    species: Mapped[str] = mapped_column(String(100), nullable=False)
    breed: Mapped[str] = mapped_column(String(100), nullable=False)
    age: Mapped[int] = mapped_column(Integer)
    # Link tables in database
    owners_id: Mapped[int] = mapped_column(ForeignKey("owners.id"), nullable=False)
    # Set pointer to pets attribute in Owner
    owner: Mapped["Owner"] = relationship("Owner", back_populates="pets")
    pets_vets: Mapped[list["Vet"]] = relationship(
        "Vet", secondary=appointment, back_populates="vets_pets"
    )


class Vet(Base):
    __tablename__ = "vets"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    specialization: Mapped[str] = mapped_column(String(100), nullable=False)
    email: Mapped[str] = mapped_column(String(150), unique=True)
    vets_pets: Mapped[list["Pet"]] = relationship(
        "Pet", secondary=appointment, back_populates="pets_vets"
    )


def create_owner(engine, name, phone, email):
    # Open session
    Session = sessionmaker(engine)
    session = Session()

    ## Add new owner
    owner = Owner(name=name, phone=phone, email=email)
    session.add(owner)
    session.commit()
    session.close()


def create_pet(engine, name, species, breed, age, owner_id):
    # Open session
    Session = sessionmaker(engine)
    session = Session()

    ## Add new pet
    pet = Pet(name=name, species=species, breed=breed, age=age, owners_id=owner_id)
    session.add(pet)
    session.commit()
    session.close()


def create_vet(engine, name, specialization, email):
    # Open session
    Session = sessionmaker(engine)
    session = Session()

    # Add vet
    vet = Vet(name=name, specialization=specialization, email=email)
    session.add(vet)
    session.commit()
    session.close()


def main():
    pass
    # create_owner(engine, "Billy Bob Jones", "555-123-4567", "bob@bob.com") 1
    # create_pet(engine, "Super Bob", "Turkey", "Bird", 10, 1)
    #
    # create_owner(engine, "Sally Sue", "555-987-6543", "sally@sally.com")
    # create_pet(engine, "Flower", "Bird", "cockatiel", 15, 2)
    # create_pet(engine, "Moron", "Dog", "Pug", 5, 2)
    #
    # create_owner(engine, "Joe Mama", "555-000-1111", "joe@mama.org")
    # create_pet(engine, "Apollo", "Cat", "Tux", 3, 3)
    # create_pet(engine, "Rocky", "Cat", "Shorthair", 3, 3)

    # create_vet(engine, "Dr. Pole", "Surgery", "pole@my_vet.com")
    # create_vet(engine, "Dr. BadAss", "Badassery", "smith@my_vet.com")


if __name__ == "__main__":
    main()

Base.metadata.create_all(engine)
