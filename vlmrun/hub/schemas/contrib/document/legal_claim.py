from datetime import date
from decimal import Decimal
from enum import Enum
from typing import Optional, List
from pydantic import BaseModel, Field


class Address(BaseModel):
    """
    Address model for both claimant and defendant addresses.
    """
    building_and_street: Optional[str] = Field(
        None, 
        description="Building name/number and street"
    )
    second_line: Optional[str] = Field(
        None, 
        description="Second line of address (e.g., Apartment/Suite)"
    )
    town_or_city: Optional[str] = Field(
        None, 
        description="Town or city"
    )
    county: Optional[str] = Field(
        None, 
        description="County (optional)"
    )
    postcode: Optional[str] = Field(
        None, 
        description="Postal code"
    )


class CourtInfo(BaseModel):
    """
    Information about the court and case reference.
    """
    court_name: Optional[str] = Field(
        None, 
        description="Name of the court (e.g., 'Cambridge County Court')"
    )
    fee_account_no: Optional[str] = Field(
        None, 
        description="Fee account number, if applicable"
    )
    help_with_fees_ref: Optional[str] = Field(
        None, 
        description="Help with fees reference number"
    )
    claim_number: Optional[str] = Field(
        None, 
        description="Court-assigned claim number"
    )
    issue_date: Optional[date] = Field(
        None, 
        description="Date the claim was issued"
    )


class FinancialDetails(BaseModel):
    """
    Financial details of the claim.
    """
    amount_claimed: Optional[Decimal] = Field(
        None, 
        description="Amount being claimed by the claimant"
    )
    court_fee: Optional[Decimal] = Field(
        None, 
        description="Court fee required for filing"
    )
    legal_representative_costs: Optional[Decimal] = Field(
        None, 
        description="Costs of legal representation"
    )
    total_amount: Optional[Decimal] = Field(
        None, 
        description="Total amount including fees and any other costs"
    )


class VulnerabilityDetails(BaseModel):
    """
    Details about vulnerability of parties involved.
    """
    is_vulnerable: Optional[bool] = Field(
        None, 
        description="Indicates if the claimant or witness has a vulnerability"
    )
    vulnerability_details: Optional[str] = Field(
        None, 
        description="Details of the vulnerability and any required adjustments"
    )
    includes_human_rights_issues: Optional[bool] = Field(
        None,
        description="Whether the claim involves issues under the Human Rights Act 1998"
    )


class SignatoryType(str, Enum):
    """
    Types of signatories for the claim.
    """
    CLAIMANT = "Claimant"
    LITIGATION_FRIEND = "Litigation friend"
    LEGAL_REPRESENTATIVE = "Claimant's legal representative"


class SignatureDetails(BaseModel):
    """
    Details about the signature and declaration.
    """
    signatory_type: Optional[List[SignatoryType]] = Field(
        None, 
        description="Type(s) of person signing (e.g., Claimant, Legal Rep)"
    )
    signature_date: Optional[date] = Field(
        None, 
        description="Date of signature"
    )
    full_name: Optional[str] = Field(
        None, 
        description="Full name of the signatory"
    )
    legal_firm_name: Optional[str] = Field(
        None, 
        description="Name of the legal firm (if signed by a representative)"
    )
    position_held: Optional[str] = Field(
        None, 
        description="Position held if signing on behalf of a firm/organization"
    )


class ContactDetails(BaseModel):
    """
    Contact details for correspondence.
    """
    phone_number: Optional[str] = Field(
        None, 
        description="Contact phone number"
    )
    dx_number: Optional[str] = Field(
        None, 
        description="DX (Document Exchange) number"
    )
    reference: Optional[str] = Field(
        None, 
        description="Internal reference number"
    )
    email: Optional[str] = Field(
        None, 
        description="Contact email address"
    )


class LegalClaim(BaseModel):
    """
    Main schema for a legal claim form, allowing None for all fields.
    """
    # Court Information
    court_info: Optional[CourtInfo] = Field(
        None, 
        description="Court and case reference information"
    )

    # Claimant Details
    claimant_name: Optional[str] = Field(
        None, 
        description="Full name of the claimant"
    )
    claimant_address: Optional[Address] = Field(
        None, 
        description="Claimant's address"
    )

    # Defendant Details
    defendant_name: Optional[str] = Field(
        None, 
        description="Full name of the defendant"
    )
    defendant_address: Optional[Address] = Field(
        None, 
        description="Defendant's address"
    )

    # Claim Details
    brief_details: Optional[str] = Field(
        None, 
        description="Brief overview of the claim"
    )
    claim_value: Optional[Decimal] = Field(
        None, 
        description="Monetary value of the claim"
    )
    claim_particulars: Optional[str] = Field(
        None, 
        description="Detailed particulars of the claim"
    )
    particulars_status: Optional[str] = Field(
        None, 
        description="Status of particulars (e.g., 'attached', 'to follow')"
    )

    # Additional Information
    hearing_centre: Optional[str] = Field(
        None, 
        description="Preferred County Court Hearing Centre"
    )
    vulnerability: Optional[VulnerabilityDetails] = Field(
        None, 
        description="Vulnerability and human rights details"
    )

    # Financial Information
    financial_details: Optional[FinancialDetails] = Field(
        None, 
        description="Breakdown of financial amounts and fees"
    )

    # Signature and Contact
    signature: Optional[SignatureDetails] = Field(
        None, 
        description="Signature and declaration details"
    )
    contact_details: Optional[ContactDetails] = Field(
        None, 
        description="Contact details for further correspondence"
    )
