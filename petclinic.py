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
engine = create_engine("sqlite:///clinic.db")

# Create Base instance
Base = declarative_base()

vets_pets = Table(
    "vets_pets",
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


class Pet(Base):
    __tablename__ = "pets"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    species: Mapped[str] = mapped_column(String(100), nullable=False)
    breed: Mapped[str] = mapped_column(String(100), nullable=False)
    age: Mapped[int] = mapped_column(Integer)

    # foreign key to owner id


class Vet(Base):
    __tablename__ = "vets"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    specialization: Mapped[str] = mapped_column(String(100), nullable=False)
    email: Mapped[str] = mapped_column(String(150), unique=True)
