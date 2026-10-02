from db import supabase


try: 
    response = (
        supabase
        .table("schemes")
        .select("id")
        .limit(1)
        .execute()
    )

    print("Supabase connection successful!")
    print("Response:", response.data)

except Exception as e:
    print("Supabase connection failed!")
    print("Error:", e)