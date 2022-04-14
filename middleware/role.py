from sqlalchemy.orm import Session

from middleware.jwtsecurity import verify_jwt
import crud.user as Crud
from schemal.roles import UserRoles

def is_admin( token : str, db : Session ):       
    jwt_decode = verify_jwt(token)     
    user = Crud.get_user_by_email(jwt_decode['email'], db)            
    if user.__dict__['user_role'] not in (UserRoles.admin, UserRoles.superadmin):
        return False
    
    return True