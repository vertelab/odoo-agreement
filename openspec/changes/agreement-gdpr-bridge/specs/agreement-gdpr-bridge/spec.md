## ADDED Requirements

### Requirement: Processing agreements are linked to inventories

A `gdpr.inventory` SHALL be able to reference the agreements that govern the
processing, in particular the data processing agreement required by Article 28.

#### Scenario: Inventory shows its processing agreement
- **WHEN** a GDPR officer opens an inventory
- **THEN** the form shows the linked agreements with type, counterparty and
  validity period

#### Scenario: Agreement is not duplicated
- **WHEN** an agreement is linked to an inventory
- **THEN** the agreement record is the single source of truth
- **AND** no copy of the agreement text is stored on the inventory

#### Scenario: One agreement serves several inventories
- **WHEN** the same processing agreement covers two processing activities
- **THEN** both inventories reference the same `agreement` record
- **AND** no second agreement is created

### Requirement: Processing agreement types are available

The system SHALL provide agreement types covering the GDPR instrument set.

#### Scenario: Standard types exist
- **WHEN** the module is installed
- **THEN** agreement types exist for: data processing agreement (Article 28),
  standard contractual clauses (Article 46), joint controller arrangement
  (Article 26), and confidentiality undertaking

#### Scenario: Type is required on a GDPR agreement
- **WHEN** an agreement is linked to an inventory
- **THEN** an agreement type is mandatory

### Requirement: Missing agreement warns, does not block

An inventory that is a processor, or that shares data with a recipient, SHALL
warn when no processing agreement is linked. A missing agreement SHALL NOT
prevent the inventory from being activated.

#### Scenario: Processor without agreement warns
- **WHEN** an inventory has role `processor` and no linked processing agreement
- **THEN** the inventory shows a warning
- **AND** the responsible officer is notified
- **AND** activation is still allowed

#### Scenario: Recipient without agreement warns
- **WHEN** an inventory lists a recipient category but no linked agreement
- **THEN** the inventory shows a warning naming the recipient categories

### Requirement: Expired agreement blocks activation

An inventory whose linked processing agreement has expired SHALL NOT be
activated.

#### Scenario: Expired agreement blocks activation
- **WHEN** an officer tries to activate an inventory whose processing agreement
  end date has passed
- **THEN** activation is refused with a message naming the expired agreement

#### Scenario: Expiring agreement is flagged
- **WHEN** a linked agreement's end date is within the configured warning window
- **THEN** the inventory shows a warning
- **AND** the responsible officer is notified

#### Scenario: No end date means no expiry
- **WHEN** a linked agreement has no end date
- **THEN** it never triggers an expiry warning or a block
