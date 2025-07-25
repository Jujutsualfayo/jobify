from logging.config import fileConfig
from sqlalchemy import create_engine
from sqlalchemy import pool

from alembic import context

from app.database import Base
from app.models import user, profile, experience, education, skill

# ------------------------------------------------------
# ✅ HARDCODE YOUR POSTGRES DATABASE URL HERE:
DATABASE_URL = "postgresql://postgres:postgres@db:5432/jobify_db"
# ------------------------------------------------------

# Alembic Config object
config = context.config

# Setup loggers
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Add your model's MetaData object
target_metadata = Base.metadata

def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode."""
    url = DATABASE_URL
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online() -> None:
    """Run migrations in 'online' mode."""
    connectable = create_engine(DATABASE_URL, poolclass=pool.NullPool)

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
