from alembic_utils.pg_extension import PGExtension

uuid_ossp_migration = PGExtension(
    schema='public',
    signature='uuid-ossp'
)