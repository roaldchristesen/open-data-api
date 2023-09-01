from sqlalchemy import CheckConstraint, Column, ForeignKey, Index, Integer, Numeric, String, Table, Text, text
from sqlalchemy.sql.sqltypes import NullType
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class AgeGroupsOfResident(Base):
    __tablename__ = 'age_groups_of_residents'

    id = Column(Integer, primary_key=True)
    year = Column(Integer, nullable=False, index=True)
    age_under_18 = Column(Integer)
    age_18_to_under_30 = Column(Integer)
    age_30_to_under_45 = Column(Integer)
    age_45_to_under_65 = Column(Integer)
    age_65_to_under_80 = Column(Integer)
    age_80_and_above = Column(Integer)


class ChildEducationSupport(Base):
    __tablename__ = 'child_education_support'

    id = Column(Integer, primary_key=True)
    year = Column(Integer, index=True)
    educational_assistance = Column(Integer)
    parenting_counselor = Column(Integer)
    pedagogical_family_assistance = Column(Integer)
    child_day_care_facility = Column(Integer)
    full_time_care = Column(Integer)
    residential_education = Column(Integer)
    integration_assistance = Column(Integer)
    additional_support = Column(Integer)


class District(Base):
    __tablename__ = 'districts'

    id = Column(Integer, primary_key=True, unique=True)
    name = Column(String)
    geometry = Column(NullType)


class HouseholdType(Base):
    __tablename__ = 'household_type'

    id = Column(Integer, primary_key=True, unique=True)
    label = Column(String)


class NonGermanNationalsResidenceStatus(Base):
    __tablename__ = 'non_german_nationals_residence_status'

    id = Column(Integer, primary_key=True)
    year = Column(Integer, index=True)
    permanent_residency = Column(Integer)
    permanent_residency_according_eu_freedom_movement_act = Column(Integer)
    permanent_residency_third_country_nationality = Column(Integer)
    without_permanent_residency = Column(Integer)
    asylum_seeker = Column(Integer)
    suspension_of_deportation = Column(Integer)


class SpatialRefSy(Base):
    __tablename__ = 'spatial_ref_sys'
    __table_args__ = (
        CheckConstraint('(srid > 0) AND (srid <= 998999)'),
    )

    srid = Column(Integer, primary_key=True)
    auth_name = Column(String(256))
    auth_srid = Column(Integer)
    srtext = Column(String(2048))
    proj4text = Column(String(2048))


class AgeGroupsOfResidentsByDistrict(Base):
    __tablename__ = 'age_groups_of_residents_by_districts'
    __table_args__ = (
        Index('age_groups_of_residents_by_districts_year_district_id_idx', 'year', 'district_id'),
    )

    id = Column(Integer, primary_key=True)
    year = Column(Integer, nullable=False)
    district_id = Column(ForeignKey('districts.id'))
    age_under_18 = Column(Integer)
    age_18_to_under_30 = Column(Integer)
    age_30_to_under_45 = Column(Integer)
    age_45_to_under_65 = Column(Integer)
    age_65_to_under_80 = Column(Integer)
    age_80_and_older = Column(Integer)
    age_0_to_under_7 = Column(Integer)
    age_60_and_older = Column(Integer)

    district = relationship('District')


class AgeRatioByDistrict(Base):
    __tablename__ = 'age_ratio_by_districts'
    __table_args__ = (
        Index('age_ratio_by_districts_year_district_id_idx', 'year', 'district_id'),
    )

    id = Column(Integer, primary_key=True)
    year = Column(Integer, nullable=False)
    district_id = Column(ForeignKey('districts.id'))
    quotient = Column(Integer)

    district = relationship('District')


class BasicBenefitsIncomeByDistrict(Base):
    __tablename__ = 'basic_benefits_income_by_districts'
    __table_args__ = (
        Index('basic_benefits_income_by_districts_year_district_id_idx', 'year', 'district_id'),
    )

    id = Column(Integer, primary_key=True)
    year = Column(Integer)
    district_id = Column(ForeignKey('districts.id'))
    male = Column(Integer)
    female = Column(Integer)
    age_18_to_under_65 = Column(Integer)
    age_65_and_above = Column(Integer)

    district = relationship('District')


class BeneficiariesAge15ToUnder65ByDistrict(Base):
    __tablename__ = 'beneficiaries_age_15_to_under_65_by_districts'
    __table_args__ = (
        Index('beneficiaries_age_15_to_under_65_by_districts_year_district_id_', 'year', 'district_id'),
    )

    id = Column(Integer, primary_key=True)
    year = Column(Integer)
    district_id = Column(ForeignKey('districts.id'))
    total = Column(Integer)
    percentage_of_total_residents = Column(Numeric)
    employable_with_benefits = Column(Integer)
    unemployment_benefits = Column(Integer)
    basic_income = Column(Integer)
    assisting_benefits = Column(Integer)

    district = relationship('District')


class BeneficiariesByDistrict(Base):
    __tablename__ = 'beneficiaries_by_districts'
    __table_args__ = (
        Index('beneficiaries_by_districts_year_district_id_idx', 'year', 'district_id'),
    )

    id = Column(Integer, primary_key=True)
    year = Column(Integer, nullable=False)
    district_id = Column(ForeignKey('districts.id'))
    residents = Column(Integer)

    district = relationship('District')


class BeneficiariesCharacteristicsByDistrict(Base):
    __tablename__ = 'beneficiaries_characteristics_by_districts'
    __table_args__ = (
        Index('beneficiaries_characteristics_by_districts_year_district_id_idx', 'year', 'district_id'),
    )

    id = Column(Integer, primary_key=True)
    district_id = Column(ForeignKey('districts.id'))
    year = Column(Integer)
    unemployability = Column(Integer)
    employability = Column(Integer)
    percentage_females = Column(Numeric)
    percenatage_single_parents = Column(Numeric)
    percentage_foreign_citizenship = Column(Numeric)

    district = relationship('District')


class BirthsByDistrict(Base):
    __tablename__ = 'births_by_districts'
    __table_args__ = (
        Index('births_by_districts_year_district_id_idx', 'year', 'district_id'),
    )

    id = Column(Integer, primary_key=True)
    year = Column(Integer, nullable=False)
    district_id = Column(ForeignKey('districts.id'))
    births = Column(Integer)
    birth_rate = Column(Numeric)

    district = relationship('District')


class ChildrenAgeUnder18ByDistrict(Base):
    __tablename__ = 'children_age_under_18_by_districts'
    __table_args__ = (
        Index('children_age_under_18_by_districts_year_district_id_idx', 'year', 'district_id'),
    )

    id = Column(Integer, primary_key=True)
    year = Column(Integer, nullable=False)
    district_id = Column(ForeignKey('districts.id'))
    residents = Column(Integer)

    district = relationship('District')


class DebtCounselingOfResidents(Base):
    __tablename__ = 'debt_counseling_residents'
    __table_args__ = (
        Index('debt_counseling_residents_year_household_type_id_idx', 'year', 'household_type_id'),
    )

    id = Column(Integer, primary_key=True)
    year = Column(Integer)
    household_type_id = Column(ForeignKey('household_type.id'))
    residents = Column(Integer)

    household_type = relationship('HouseholdType')


class EmployedWithPensionInsuranceByDistrict(Base):
    __tablename__ = 'employed_with_pension_insurance_by_districts'
    __table_args__ = (
        Index('employed_with_pension_insurance_by_districts_year_district_id_i', 'year', 'district_id'),
    )

    id = Column(Integer, primary_key=True)
    year = Column(Integer, nullable=False)
    district_id = Column(ForeignKey('districts.id'))
    residents = Column(Integer)
    employment_rate = Column(Numeric)

    district = relationship('District')


class HouseholdsAtRiskOfHomelessnessByDistrict(Base):
    __tablename__ = 'households_at_risk_of_homelessness_by_districts'
    __table_args__ = (
        Index('households_at_risk_of_homelessness_by_districts_year_district_i', 'year', 'district_id'),
    )

    id = Column(Integer, primary_key=True)
    year = Column(Integer)
    district_id = Column(ForeignKey('districts.id'))
    residents = Column(Integer)

    district = relationship('District')


class HousingAssistanceCasesByDistrict(Base):
    __tablename__ = 'housing_assistance_cases_by_districts'
    __table_args__ = (
        Index('housing_assistance_cases_by_districts_year_district_id_idx', 'year', 'district_id'),
    )

    id = Column(Integer, primary_key=True)
    year = Column(Integer)
    district_id = Column(ForeignKey('districts.id'))
    general_consulting = Column(Integer)
    notices_of_rent_arrears = Column(Integer)
    termination_rent_arrears = Column(Integer)
    termination_for_conduct = Column(Integer)
    action_for_eviction = Column(Integer)
    eviction_notice = Column(Integer)
    eviction_carried = Column(Integer)

    district = relationship('District')


class HousingBenefitByDistrict(Base):
    __tablename__ = 'housing_benefit_by_districts'
    __table_args__ = (
        Index('housing_benefit_by_districts_year_district_id_idx', 'year', 'district_id'),
    )

    id = Column(Integer, primary_key=True)
    year = Column(Integer)
    district_id = Column(ForeignKey('districts.id'))
    residents = Column(Integer)

    district = relationship('District')


class InactiveBeneficiariesInHouseholdsByDistrict(Base):
    __tablename__ = 'inactive_beneficiaries_in_households_by_districts'
    __table_args__ = (
        Index('inactive_beneficiaries_in_households_by_districts_year_district', 'year', 'district_id'),
    )

    id = Column(Integer, primary_key=True)
    year = Column(Integer, nullable=False)
    district_id = Column(ForeignKey('districts.id'))
    residents = Column(Integer)

    district = relationship('District')


class MigrationBackgroundByDistrict(Base):
    __tablename__ = 'migration_background_by_districts'
    __table_args__ = (
        Index('migration_background_by_districts_year_district_id_idx', 'year', 'district_id'),
    )

    id = Column(Integer, primary_key=True)
    year = Column(Integer, nullable=False)
    district_id = Column(ForeignKey('districts.id'))
    foreign_citizenship = Column(Integer)
    german_citizenship = Column(Integer)

    district = relationship('District')


class ResidentsAge18ToUnder65ByDistrict(Base):
    __tablename__ = 'residents_age_18_to_under_65_by_districts'
    __table_args__ = (
        Index('residents_age_18_to_under_65_by_districts_year_district_id_idx', 'year', 'district_id'),
    )

    id = Column(Integer, primary_key=True)
    year = Column(Integer, nullable=False)
    district_id = Column(ForeignKey('districts.id'))
    residents = Column(Integer)

    district = relationship('District')


class ResidentsAge65AndAboveByDistrict(Base):
    __tablename__ = 'residents_age_65_and_above_by_districts'
    __table_args__ = (
        Index('residents_age_65_and_above_by_districts_year_district_id_idx', 'year', 'district_id'),
    )

    id = Column(Integer, primary_key=True)
    year = Column(Integer, nullable=False)
    district_id = Column(ForeignKey('districts.id'))
    residents = Column(Integer)

    district = relationship('District')


class ResidentsByDistrict(Base):
    __tablename__ = 'residents_by_districts'
    __table_args__ = (
        Index('residents_by_districts_year_district_id_idx', 'year', 'district_id'),
    )

    id = Column(Integer, primary_key=True)
    year = Column(Integer, nullable=False)
    district_id = Column(ForeignKey('districts.id'))
    residents = Column(Integer)

    district = relationship('District')


class UnemployedResidentsByDistrict(Base):
    __tablename__ = 'unemployed_residents_by_districts'
    __table_args__ = (
        Index('unemployed_residents_by_districts_year_district_id_idx', 'year', 'district_id'),
    )

    id = Column(Integer, primary_key=True)
    year = Column(Integer, nullable=False)
    district_id = Column(ForeignKey('districts.id'))
    residents = Column(Integer)

    district = relationship('District')


class UnemployedCategorizedResidentsByDistrict(Base):
    __tablename__ = 'unemployed_residents_by_districts_categorized'
    __table_args__ = (
        Index('unemployed_residents_by_districts_categorized_year_district_id_', 'year', 'district_id'),
    )

    id = Column(Integer, primary_key=True)
    year = Column(Integer)
    district_id = Column(ForeignKey('districts.id'))
    total = Column(Integer)
    unemployed_total = Column(Integer)
    percentage_of_total = Column(Numeric)
    percentage_sgb_iii = Column(Numeric)
    percentage_sgb_ii = Column(Numeric)
    percentage_foreign_citizenship = Column(Numeric)
    percentage_female = Column(Numeric)
    percentage_age_under_25 = Column(Numeric)

    district = relationship('District')
