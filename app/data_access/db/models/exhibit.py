from sqlalchemy import Column, String, ForeignKey, TIMESTAMP
from sqlalchemy.dialects.postgresql import UUID
import uuid
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from data_access.db.base import Base

class Exhibit(Base):
    __tablename__ = "exhibits"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String(255), nullable=False)
    era = Column(String(100), nullable=False)
    museum_id = Column(UUID(as_uuid=True), ForeignKey("museums.id"), nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), server_default=func.now())

    museum = relationship("Museum", back_populates="exhibits")