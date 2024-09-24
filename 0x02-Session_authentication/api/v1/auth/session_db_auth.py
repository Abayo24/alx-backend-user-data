#!/usr/bin/env python3
"""Module SessionDBAuth"""
from api.v1.auth.session_exp_auth import SessionExpAuth
from models.user_session import UserSession
from models import storage


class SessionDBAuth(SessionExpAuth):
    """Module SessionDBAuth"""
    def create_session(self, user_id=None):
        """Create a new session and store it in UserSession"""
        session_id = super().create_session(user_id)
        if not session_id:
            return None
        user_session = UserSession(user_id=user_id, session_id=session_id)
        user_session.save()
        return session_id

    def user_id_for_session_id(self, session_id=None):
        """Return the user_id associated with a session_id"""
        if not session_id:
            return None
        all_sessions = storage.all(UserSession)
        for session in all_sessions.values():
            if session.session_id == session_id:
                return session.user_id
        return None

    def destroy_session(self, request=None):
        """Destroy a session based on the session ID in the request cookie"""
        if request is None:
            return False
        session_id = self.session_cookie(request)
        if not session_id:
            return False

        # Search for session in storage and delete it
        all_sessions = storage.all(UserSession)
        for session_key, session in all_sessions.items():
            if session.session_id == session_id:
                storage.delete(session)
                return True
        return False
