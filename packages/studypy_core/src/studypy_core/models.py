import datetime
import uuid

from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Table
from sqlalchemy.orm import (Mapped, declarative_base, mapped_column,
                            relationship)

Base = declarative_base()


def generate_uuid():
    return uuid.uuid4().int >> 64


class Difficulty(Base):
    __tablename__ = "difficulties"

    id: Mapped[int] = mapped_column(primary_key=True)


class StudysetFlashcard(Base):
    __tablename__ = "studyset_flashcards"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    studyset_id: Mapped[int] = mapped_column(Integer, ForeignKey("studysets.id"))
    flashcard_id: Mapped[int] = mapped_column(Integer, ForeignKey("flashcards.id"))


class Studyset(Base):
    __tablename__ = "studysets"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False, default="mystudyset")
    flashcards = relationship(
        "Flashcard", secondary="studyset_flashcards", back_populates="studysets"
    )

    def __repr__(self):
        return f"<Studyset(id={self.id}, name='{self.name}')>"


class Flashcard(Base):
    __tablename__ = "flashcards"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    question: Mapped[str] = mapped_column(
        String, nullable=False, default="my question?"
    )
    answer: Mapped[str] = mapped_column(String, nullable=False, default="my answer!")
    studysets = relationship(
        "Studyset", secondary="studyset_flashcards", back_populates="flashcards"
    )

    def __repr__(self):
        return f"<Flashcard(id={self.id}, question='{self.question}', answer='{self.answer}')>"
