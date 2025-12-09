"""
Database migration script to add indexes for better performance
Run this once to add indexes to existing database
"""

from app import app, db

def add_indexes():
    with app.app_context():
        # get the database connection
        connection = db.engine.connect()

        try:
            # add index on post status for filtering active posts
            print("Adding index on post.status...")
            connection.execute(db.text("CREATE INDEX IF NOT EXISTS idx_post_status ON post(status)"))

            # add index on post vote_score for sorting by popular
            print("Adding index on post.vote_score...")
            connection.execute(db.text("CREATE INDEX IF NOT EXISTS idx_post_vote_score ON post(vote_score)"))

            # add index on post author_id for finding user's posts
            print("Adding index on post.author_id...")
            connection.execute(db.text("CREATE INDEX IF NOT EXISTS idx_post_author_id ON post(author_id)"))

            connection.commit()
            print("All indexes added successfully!")

        except Exception as e:
            print(f"Error adding indexes: {e}")
            connection.rollback()
        finally:
            connection.close()

if __name__ == '__main__':
    print("Starting database index migration...")
    add_indexes()
    print("Migration complete!")
