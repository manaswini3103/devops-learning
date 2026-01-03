# Testing Strategies

Testing strategies are structured approaches that define what to test, how to test, and when to test in order to ensure software quality, reliability, and performance throughout the software development lifecycle (SDLC).

![DevOps Tools Pipeline](../images/TestingStrategies.jpg)

## Goals of Testing Strategies

- Detect defects early
- Ensure requirements are met
- Improve software quality
- Reduce cost of fixing bugs
- Increase user confidence


## Major Testing Strategies in Software

Unit → Integration → System → Acceptance

### Unit Testing
- What: Tests individual units or functions
- Who: Developers, When: During development
- Fast, Easy to automate
- Example: Testing a single method

### Integration Testing
- What: Tests interactions between modules
- Who: Developers / Testers, When: After unit testing
- Types:Top-down, Bottom-up, Big-bang

### System Testing
- What: Tests the complete system as a whole
- Who: Testers, When: After integration
- Validates end-to-end functionality

### Acceptance Testing
- What: Verifies system meets business requirements
- Who: Customers / QA / Product Owners, When: Before release
- Types: User Acceptance Testing (UAT), Alpha & Beta testing


## Functional Testing Strategies

1. Black Box Testing
- Tests functionality without knowing internal code
- Example: UI, API testing
2. White Box Testing
- Tests internal logic and code structure
- Example: unit tests, code coverage
3. Grey Box Testing
- Combination of both


## Non-Functional Testing Strategies

- Performance Testing: Load, stress, endurance testing, scalability.
- Security Testing: Identifying vulnerabilities.
- Usability Testing & Accessibility Testing: Ease of use and access.


## Regression Testing

- Ensure new changes do not break existing features, it's often automated.
- When: After every change


## Smoke & Sanity Testing
- Smoke: Basic build verification
- Sanity: Verify specific fixes
