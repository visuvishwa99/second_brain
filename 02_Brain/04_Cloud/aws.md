---
tags:
  - cloud
---

# Amazon S3

- ## Storage Classes
    - ![image.png](../../../assets/image_1739415934255_0.png)

- ## Encryption
    - ![image.png](../../../assets/image_1739415718762_0.png)
    - ### Best Practices for Implementing Encryption
        1. **Understand Your Data**: Assess sensitivity and compliance needs.
        2. **Choose the Right Method**:
            - **SSE-S3** for simplicity.
            - **SSE-KMS** or **DSSE-KMS** for compliance and control.
            - **SSE-C** or client-side encryption for full control over keys.
        3. **Enable Encryption by Default**: Configure S3 buckets to enforce encryption policies automatically.
        4. **Audit Regularly**: Monitor and verify encryption settings using tools like AWS CloudTrail or S3 Storage Lens.
    - **AES-GCM (AES-256)**: Widely used across AWS services for encrypting data at rest and in transit.

- ### Related
    - [[Cloud_engineering]]
    - [[Batch_processing]]

## IAM

- ![IAM_roles.jpeg](../../../assets/IAM_roles_1739418168094_0.jpeg)

## AWS Lambda Scaling
Lambda is designed for horizontal scalability ("Scale Out"), not vertical scalability ("Scale Up").

- **Horizontal Scaling (Automatic)**: 
    - Lambda creates new instances for concurrent requests.
    - 1,000 concurrent requests → up to 1,000 instances (subject to account limits).
- **Vertical Scaling (Manual)**:
    - Configured via memory allocation (128 MB to 10 GB).
    - CPU and network power scale proportionally with memory.
- **Constraints**: 
    - No dynamic vertical scaling at runtime.
    - Not suitable for massive single-instance compute or extremely long-running processes (use EC2, ECS, or EKS instead).
