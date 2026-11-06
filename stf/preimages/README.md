# Preimages STF Test Vectors

## Schema

Both the binary and json formats adhere to the overarching JAM protocol ASN.1
[schema](../jam-types-asn/jam-types.asn), as well as the specific vectors
[schema](./preimages.asn) defined for these test cases.

## Statistics

A subset of service activity statistics ($π_S$) updated by the STF subsystem used
to process these test vectors.

In particular the `provided-count` (p.0) and `provided-size` (p.1) items are
updated when new preimages are provided to be included in the chain storage via
the extrinsic.

## Limits

The extrinsic holds at most 256 preimages (`max-preimages-count`), with at most
2^25 octets of preimage data in total. Over the data limit the STF fails with
`preimages-too-big`. No vector covers this error, because such a vector is
larger than 32 MiB.

## Vectors

- [preimage_needed-1](./tiny/preimage_needed-1.json) 🟢
  - Nothing is provided.
- [preimage_needed-2](./tiny/preimage_needed-2.json) 🟢
  - Provide one solicited blob.
- [preimage_not_needed-1](./tiny/preimage_not_needed-1.json) 🔴
  - Provide two blobs, but one of them has not been solicited.
- [preimage_not_needed-2](./tiny/preimage_not_needed-2.json) 🔴
  - Provide two blobs, but one of them has already been provided.
- [preimages_order_check-1](./tiny/preimages_order_check-1.json) 🔴
  - Bad order of services.
- [preimages_order_check-2](./tiny/preimages_order_check-2.json) 🔴
  - Bad order of images for a service.
- [preimages_order_check-3](./tiny/preimages_order_check-3.json) 🟢
  - Order is correct.
- [preimages_order_check-4](./tiny/preimages_order_check-4.json) 🔴
  - Duplicate item.
- [preimages_max_count-1](./tiny/preimages_max_count-1.json) 🟢
  - Provide 256 solicited blobs for two services, the maximum number of items.
