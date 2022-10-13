print(f"""
{10*"="} DAFTAR PESERTA {"="*10}
""")

user1 = [1, "Abdul", 19, "Laki-Laki"]
user2 = [2, "Hafiz", 19, "Laki-Laki"]
user3 = [3, "Ramadan", 19, "Laki-Laki"]

users = [user1, user2, user3]

for user in users:
    print(f"""
    {user[0]}.\tNama \t\t: {user[1]}
    Umur \t\t: {user[2]}
    Kelamin \t: {user[3]} 
    """.strip())
