from datetime import datetime
from decimal import Decimal
from enum import Enum
from typing import Optional, List, Union

from pydantic import BaseModel, Field


class Party(BaseModel):
    """Information about a party (plaintiff or defendant) in the legal claim"""
    name: Optional[str] = Field(None, description="Full name of the individual or entity")
    phone: Optional[str] = Field(None, description="Phone number of the party")
    street_address: Optional[str] = Field(None, description="Street address of the party")
    city: Optional[str] = Field(None, description="City of the party's address")
    state: Optional[str] = Field(None, description="State abbreviation of the party's address")
    zip_code: Optional[str] = Field(None, description="ZIP/Postal code of the party's address")
    mailing_address: Optional[str] = Field(None, description="Mailing address if different from street address")
    email: Optional[str] = Field(None, description="Email address of the party, if provided")


class Agent(BaseModel):
    """Agent authorized for service of process (for corporations, LLCs, or public entities)"""
    name: Optional[str] = Field(None, description="Name of the agent authorized for service of process")
    job_title: Optional[str] = Field(None, description="Job title of the agent, if known")
    address: Optional[str] = Field(None, description="Full address of the agent")


class TrialDate(BaseModel):
    """Details of the scheduled trial date"""
    date: Optional[datetime] = Field(None, description="Date of the trial")
    time: Optional[str] = Field(None, description="Time of the trial (e.g., '9:00 AM')")
    department: Optional[str] = Field(None, description="Court department handling the case")
    court_address: Optional[str] = Field(None, description="Name and address of the court, if different from filing courthouse")


class ClaimReason(str, Enum):
    """Common reasons for filing a small claims case"""
    PROPERTY_DAMAGE = "Property Damage"
    CONTRACT_BREACH = "Contract Breach"
    PERSONAL_INJURY = "Personal Injury"
    DEBT = "Debt"
    OTHER = "Other"


class LegalClaimForm(BaseModel):
    """Schema for extracting structured information from a Legal Claim Form (e.g., SC-100)"""

    # Form Metadata
    form_type: Optional[str] = Field(None, description="Type of legal form (e.g., 'SC-100')")
    case_number: Optional[str] = Field(None, description="Unique case number assigned to the claim")

    # Plaintiff Information
    plaintiffs: Optional[List[Party]] = Field(None, description="List of plaintiffs filing the claim")
    is_fictitious_name: Optional[bool] = Field(None, description="Whether any plaintiff is doing business under a fictitious name")
    is_payday_lender: Optional[bool] = Field(None, description="Whether any plaintiff is a licensee or deferred deposit originator under Financial Code sections 23000 et seq.")

    # Defendant Information
    defendants: Optional[List[Party]] = Field(None, description="List of defendants being sued")
    agent_for_service: Optional[Agent] = Field(None, description="Agent authorized for service of process if defendant is a corporation, LLC, or public entity")
    is_military_duty: Optional[bool] = Field(None, description="Whether any defendant is on active military duty")

    # Claim Details
    claim_amount: Optional[Decimal] = Field(None, description="Total amount of money claimed by the plaintiff")
    reason: Optional[str] = Field(None, description="Explanation of why the defendant owes the plaintiff money")
    reason_category: Optional[ClaimReason] = Field(None, description="Category of the claim reason")
    event_date: Optional[datetime] = Field(None, description="Date when the event leading to the claim occurred")
    calculation_method: Optional[str] = Field(None, description="Explanation of how the claim amount was calculated")
    demand_made: Optional[bool] = Field(None, description="Whether the plaintiff asked the defendant to pay before filing the claim")
    demand_explanation: Optional[str] = Field(None, description="Explanation if no demand was made prior to filing")

    # Court Information
    filing_courthouse_reason: Optional[str] = Field(None, description="Reason for filing at this courthouse (e.g., where defendant lives, where event occurred)")
    filing_zip_code: Optional[str] = Field(None, description="ZIP code of the location tied to the filing reason")
    trial_date: Optional[TrialDate] = Field(None, description="Details of the scheduled trial date")

    # Additional Details
    is_attorney_fee_dispute: Optional[bool] = Field(None, description="Whether the claim is about an attorney-client fee dispute")
    is_public_entity: Optional[bool] = Field(None, description="Whether the defendant is a public entity")
    public_entity_claim_date: Optional[datetime] = Field(None, description="Date a written claim was filed with the public entity, if applicable")
    prior_claims_count: Optional[int] = Field(None, description="Number of small claims filed by plaintiff in the last 12 months in California")
    signature_date: Optional[datetime] = Field(None, description="Date the plaintiff signed the form")