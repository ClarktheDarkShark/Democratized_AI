import enum
from sqlalchemy import Column, DateTime, Enum, ForeignKey, Integer, JSON, String, Text, func
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True)
    role = Column(String)

class Agent(Base):
    __tablename__ = "agents"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    config = Column(JSON, nullable=False)
    created_by = Column(String)
    created_at = Column(DateTime, server_default=func.now())
    runs = relationship("Run", back_populates="agent")

class RunStatus(str, enum.Enum):
    pending = "pending"
    running = "running"
    waiting_approval = "waiting_approval"
    approved = "approved"
    rejected = "rejected"
    succeeded = "succeeded"
    failed = "failed"

class Run(Base):
    __tablename__ = "runs"
    id = Column(Integer, primary_key=True)
    agent_id = Column(Integer, ForeignKey("agents.id"))
    status = Column(Enum(RunStatus), default=RunStatus.pending)
    input = Column(JSON)
    output = Column(JSON)
    created_at = Column(DateTime, server_default=func.now())
    agent = relationship("Agent", back_populates="runs")

class Approval(Base):
    __tablename__ = "approvals"
    id = Column(Integer, primary_key=True)
    run_id = Column(Integer, ForeignKey("runs.id"))
    requested_by = Column(String)
    approver = Column(String)
    status = Column(String, default="pending")
    payload = Column(JSON)
    created_at = Column(DateTime, server_default=func.now())

class AuditLog(Base):
    __tablename__ = "audit_logs"
    id = Column(Integer, primary_key=True)
    actor = Column(String)
    action = Column(String)
    resource = Column(String)
    payload = Column(JSON)
    hash = Column(String)
    created_at = Column(DateTime, server_default=func.now())

class Document(Base):
    __tablename__ = "documents"
    id = Column(Integer, primary_key=True)
    source = Column(String)
    uri = Column(String)
    meta = Column(JSON)

class Embedding(Base):
    __tablename__ = "embeddings"
    document_id = Column(Integer, ForeignKey("documents.id"), primary_key=True)
    chunk_id = Column(Integer, primary_key=True)
    vector = Column(Text)
