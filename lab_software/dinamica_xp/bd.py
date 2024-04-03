from supabase import create_client, Client
from settings import SUPABASE_URL, SUPABASE_KEY

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

response = supabase.table('cliente').select("*").execute()
response2 = supabase.table('cliente').insert({'nome':'Arthur'}).execute()