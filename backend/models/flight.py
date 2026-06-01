"""SQLAlchemy ORM models for the flight booking domain.

The models are intentionally simple – they capture the core entities
required for the API.  Relationships are defined using the new
SQLAlchemy 2.0 style declarative base.
"""

from __future__ import annotations

from datetime import datetime
from typing import Optional

from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Boolean, Float
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    """Base class for all ORM models."""

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class Airline(Base):
    """Airline operating flights."""

    name: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    iata_code: Mapped[str] = mapped_column(String(2), unique=True, nullable=False)

    flights: Mapped[list["Flight"]] = relationship(back_populates="airline", cascade="all, delete-orphan")


class Flight(Base):
    """A scheduled flight."""

    flight_number: Mapped[str] = mapped_column(String(10), nullable=False)
    departure_airport: Mapped[str] = mapped_column(String(3), nullable=False)
    arrival_airport: Mapped[str] = mapped_column(String(3), nullable=False)
    departure_time: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    arrival_time: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    status: Mapped[str] = mapped_column(String(20), default="scheduled")

    airline_id: Mapped[int] = mapped_column(ForeignKey("airline.id"), nullable=False)
    airline: Mapped[Airline] = relationship(back_populates="flights")

    bookings: Mapped[list["Booking"]] = relationship(back_populates="flight", cascade="all, delete-orphan")


class User(Base):
    """Registered user of the system."""

    email: Mapped[str] = mapped_column(String(255), unique=True, nullable=False)
    hashed_password: Mapped[str] = mapped_column(String(255), nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    is_superuser: Mapped[bool] = mapped_column(Boolean, default=False)

    bookings: Mapped[list["Booking"]] = relationship(back_populates="user", cascade="all, delete-orphan")


class Booking(Base):
    """A ticket booking for a flight."""

    passenger_name: Mapped[str] = mapped_column(String(100), nullable=False)
    seat_number: Mapped[Optional[str]] = mapped_column(String(5))
    price: Mapped[float] = mapped_column(Float, nullable=False)
    paid: Mapped[bool] = mapped_column(Boolean, default=False)

    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"), nullable=False)
    user: Mapped[User] = relationship(back_populates="bookings")

    flight_id: Mapped[int] = mapped_column(ForeignKey("flight.id"), nullable=False)
    flight: Mapped[Flight] = relationship(back_populates="bookings")


__all__ = ["Base", "Airline", "Flight", "User", "Booking"]
