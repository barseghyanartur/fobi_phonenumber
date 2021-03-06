Release history and notes
=========================
`Sequence based identifiers
<http://en.wikipedia.org/wiki/Software_versioning#Sequence-based_identifiers>`_
are used for versioning (schema follows below):

.. code-block:: text

    major.minor[.revision]

- It's always safe to upgrade within the same minor version (for example, from
  0.3 to 0.3.4).
- Minor version changes might be backwards incompatible. Read the
  release notes carefully before upgrading (for example, when upgrading from
  0.3.4 to 0.4).
- All backwards incompatible changes are mentioned in this document.

0.2
---
2017-05-30

- Fixed typo (leads to backwards incompatibility!). Change UID of the
  PhoneNumberPlugin from ``fomi_phonenumber`` to ``fobi_phonenumber``.
  Update your database accordingly.
- Minor package updates/improvements (added wheels support, clean-up).

0.1.0
-----
2016-02-10

- Initial release.
