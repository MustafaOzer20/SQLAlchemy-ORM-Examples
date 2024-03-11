from models import (
    User,
    Profile
)
from database import Session


def profile_to_user():
    session = Session()
    
    profile_list = session.query(Profile).all()
    
    for profile in profile_list:
        print({
            "Username": profile.user.name,
            "Address": profile.address
        })

    session.close()


def user_to_profile():
    session = Session()
    
    user = session.query(User).filter_by(name='John').first()
    print({
        "Username": user.name,
        "Address": user.profile.address
    })

    session.close()


def main():
    profile_to_user()
    print(50*"-")
    user_to_profile()


if __name__ == "__main__":
    main()