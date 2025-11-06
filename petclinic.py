# Required imports
from re import S
from sqlalchemy import (
    create_engine,
    Integer,
    String,
    ForeignKey,
    DateTime,
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
from datetime import datetime

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


Base.metadata.create_all(engine)
