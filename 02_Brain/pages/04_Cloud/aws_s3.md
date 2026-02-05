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
