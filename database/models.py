from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship
from database.database import Base

class Campaign(Base):
    __tablename__ = 'campaigns'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    objective = Column(String)

    adsets = relationship("Adset", back_populates="campaign")

    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "objective": self.objective,
            "adsets": [adset.to_json() for adset in self.adsets]
        }

class Adset(Base):
    __tablename__ = 'adsets'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    optimization_goal = Column(String)

    campaign_id = Column(Integer, ForeignKey('campaigns.id'))

    campaign = relationship("Campaign", back_populates="adsets")
    groups = relationship("Group", secondary="adset_group", back_populates="adsets")

    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "optimization_goal": self.optimization_goal,
            "campaign": self.campaign_id,
            "groups": [group.id for group in self.groups] if self.groups else []
        }

class Group(Base):
    __tablename__ = 'groups'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

    adsets = relationship("Adset", secondary="adset_group", overlaps="groups")

    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "adsets": [adset.to_json() for adset in self.adsets]
        }

adset_group = Table('adset_group', Base.metadata,
    Column('adset_id', Integer, ForeignKey('adsets.id')),
    Column('group_id', Integer, ForeignKey('groups.id'))
)
