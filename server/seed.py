from datetime import datetime
from app import app
from models import db, Guest, Episode, Appearance

# Sample data (you can convert this to read from a CSV if needed)
sample_data = [
    {"year": 1999, "occupation": "actor", "date": "1/11/99", "group": "Acting", "guest_names": "Michael J. Fox"},
    {"year": 1999, "occupation": "comedian", "date": "2/1/99", "group": "Comedy", "guest_names": "George Carlin"},
    {"year": 1999, "occupation": "actress", "date": "2/10/99", "group": "Acting", "guest_names": "Pamela Anderson, Natalie Raitano, Molly Culver"},
    # ... add more
]

if __name__ == '__main__':
    with app.app_context():
        print("Clearing database...")
        Appearance.query.delete()
        Episode.query.delete()
        Guest.query.delete()

        print("Seeding data...")

        for row in sample_data:
            # Create or get episode
            date_obj = datetime.strptime(row["date"], "%m/%d/%y")
            episode = Episode(date=date_obj, number=0)  # You can update number logic later
            db.session.add(episode)

            guest_names = [name.strip() for name in row["guest_names"].split(",")]
            for name in guest_names:
                # Create or get guest
                guest = Guest(name=name, occupation=row["occupation"])
                db.session.add(guest)

                # Create appearance
                appearance = Appearance(guest=guest, episode=episode, rating=4.0)  # You can randomize rating if needed
                db.session.add(appearance)

        db.session.commit()
        print("Seeding complete!")
