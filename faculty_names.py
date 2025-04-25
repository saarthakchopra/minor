# import requests
# from bs4 import BeautifulSoup

# # Base URL
# base_url = "https://www.jiit.ac.in/computer-science-and-it-faculty"

# # List to store all faculty names
# faculty_names = []

# # Loop through 7 pages
# for page_num in range(0, 7):
#     if page_num == 0:
#         url = base_url
#     else:
#         url = f"{base_url}?page={page_num}"
    
#     print(f"Scraping page {page_num + 1}...")

#     response = requests.get(url)
#     soup = BeautifulSoup(response.text, 'html.parser')

#     # Find all divs with class "faculty-name"
#     faculty_divs = soup.find_all("div", class_="faculty-name")

#     for div in faculty_divs:
#         name = div.get_text(strip=True)
#         faculty_names.append(name)

# # Save to a .txt file with names in "" and comma-separated
# with open("faculty_names.txt", "w", encoding="utf-8") as file:
#     formatted_names = ', '.join(f'"{name}"' for name in faculty_names)
#     file.write(formatted_names)

# print("\nFaculty names saved to faculty_names.txt")



# part 2 that was required for later to filter with NOT FOUND


data = """Name,GSID
Prof. Sandeep Kumar Singh,Not Found
Prof. Krishna Asawa,Not Found
Prof. Manish Kumar Thakur,MYxL_ZkAAAAJ
Prof. Shikha Mehta,nBy-KdgAAAAJ
Prof. Anuja Arora,Uz_ML8cAAAAJ
Prof. Lokendra Kumar,z6mGkvAAAAAJ
Prof. Bhagwati Prasad Chamola,Z9NZ3lwAAAAJ
Prof. Pato Kumari,Not Found
Prof. Devpriya Soni,D5lGxLYAAAAJ
Prof. Neetu Sardana,HJydVWwAAAAJ
Prof. Dharmveer Singh Rajpoot,cHCjD5IAAAAJ
Prof. Mukesh Saraswat,UHKGhhEAAAAJ
Dr. Tribhuwan Kumar Tewari,v_hclFIAAAAJ
Dr. Prakash Kumar,lWX9KlgAAAAJ
Dr. K. Rajalakshmi,Not Found
Dr. Parmeet Kaur,ATKNSzcAAAAJ
Dr. Mukta Goyal,USGXgXcAAAAJ
Dr. Anita Sahoo,maZrlYcAAAAJ
Dr. Himani Bansal,r2eb30AAAAAJ
Dr. Taj Alam,jsbu8UUAAAAJ
Dr. Suma Dawn,hgaPUCQAAAAJ
Dr. Arti Jain,W8W93c0AAAAJ
Dr. Hema Nagaraja,IbhjFkcAAAAJ
Dr. Pawan Kumar Upadhyay,Not Found
Dr. Kavita Pandey,P3qMVlAAAAAJ
Dr. Indu Chawla,wsXMoFYAAAAJ
Dr. Shikha Jain,qy2r8wsAAAAJ
Dr. Megha Rathi,lnPlF_IAAAAJ
Dr. Dhanalekshmi G,Not Found
Dr. Himanshu Agrawal,eag0Zf0AAAAJ
Dr. Anubhuti Roda Mohindra,Not Found
Dr. Niyati Aggrawal,-tuoeHAAAAAJ
Dr. Gaurav Kumar Nigam,dyjwbCgAAAAJ
Dr. Amanpreet Kaur,ywgr--sAAAAJ
Dr. Pulkit Mehndiratta,LoUdggcAAAAJ
Dr. Arpita Jadhav Bhatt,KITRdYwAAAAJ
Ms. Anuradha Gupta,Not Found
Dr. Shardha Porwal,W0IihqMAAAAJ
Dr. Sakshi Gupta,SjAH3VMAAAAJ
Dr. Parul Agarwal,q1OCvewAAAAJ
Dr. Ankita,tRStpZgAAAAJ
Dr. Somya Jain,E_EI_c4AAAAJ
Prashant Kaushik,Not Found
Dr. Aditi Sharma,-AxgdDgAAAAJ
Dr. Varsha Garg,szgyrN0AAAAJ
Dr. Kashav Ajmera,bJm4wTQAAAAJ
Dr. Kirti Aggarwal,9UrL68QAAAAJ
Dr. P. Raghu Vamsi,ngT8wRgAAAAJ
Dr. Payal Khurana Batra,-SiS0o8AAAAJ
Dr. Ankit Vidyarthi,h8NBQjMAAAAJ
Dr. Ankita Verma,oLh8CBsAAAAJ
Dr. Amarjeet Prajapati,RoeOU3UAAAAJ
Dr. Neeraj Jain,Not Found
Dr. Rashmi Kushwah,I33yPegAAAAJ
Dr. Shruti Jaiswal,D_xBJQgAAAAJ
Dr. Sonal,AlQ4YmQAAAAJ
Dr. Vivek Kumar Singh,3NOBikYAAAAJ
Dr. Alka Singhal,ZayqdbAAAAAJ
Dr. Ashish Mishra,i7NJLgMAAAAJ
Dr. Sulabh Tyagi,KBmTZoUAAAAJ
Dr Bhawna Saxena,Z_TtRgMAAAAJ
Dr. Vikash,lT3evUEAAAAJ
Ashish Kumar,Not Found
Dr. Kapil Madan,Not Found
Dr. Pratik Shrivastava,Not Found
Dr. Amit Mishra,x4dAEV8AAAAJ
Dr. Ashish Singh Parihar,Not Found
Dr. Asmita Yadav,E1WyOOYAAAAJ
Dr. Anil Kumar Mahto,Not Found
Dr. Jagriti,Not Found
Dr. Meenal Jain,SB1PiC0AAAAJ
Dr. Ankita Jaiswal,tRStpZgAAAAJ
Dr. Deepika Varshney,Not Found
Akanksha Mehndiratta,tNZVmx8AAAAJ
Amarjeet Kaur,c1d1oowAAAAJ
Dr. Sherry Garg,kgbKqwUAAAAJ
Dr. Naveen Chauhan,kXv5wZMAAAAJ
Dr. Shobhit Tyagi,yXwrPRUAAAAJ
Purtee Jethi Kohli,Not Found
Prantik Biswas,1fUCvWoAAAAJ
Dr. Neeraj Pathak,Not Found
Dr. Akash Kumar,Not Found
Dr. Tanvi Gautam,D1DP1PQAAAAJ
Dr. Jasmin,RohoDFoAAAAJ
Dr. Kedar Nath Singh,Not Found
Dr. Sayani Ghosal,-vqrgeMAAAAJ
Dr. Aastha Maheshwari,woTJ3kQAAAAJ
Dr. Shruti Gupta,qGfXfW8AAAAJ
Dr. Tarun Agrawal,etbX3FsAAAAJ
Dr. Diksha Chawla,Not Found
Dr. Varun Srivastava,pJumMVEAAAAJ
Dr. Mradula Sharma,sNfoBFoAAAAJ
Kirti Jain,Not Found
Deepti,r_Sa3pAAAAAJ
Shariq Murtuza,z-lpll4AAAAJ
Sarishty Gupta,oa0UwSUAAAAJ
Amitesh,Not Found
Ambalika Sarkar Bachar,Not Found
Pushp S. Mathur,Not Found
Dr. Lalita Mishra,NHp1bxYAAAAJ
Twinkle Tyagi,Not Found
Rajiv Kumar Mishra,1lG-NlAAAAAJ
Astha Singh,Not Found
Anupama Padha,jUqhSkcAAAAJ
Aarti Goel,Not Found
Janardan Kumar Verma,6ArvoPAAAAAJ
Neha,G7PTxGgAAAAJ
Akshit Raj Patel,Not Found
Sumeshwar Singh,Not Found
Ayushi Pandey,Not Found
Aditi Priya,Not Found
Shivendra Vikram Singh,Not Found
Sonal Saurabh,Not Found
Satya Prakash Patel,Not Found
Mohit Singh,Not Found
Pankaj Mishra,ZXaesfAAAAAJ
Shweta Rani,Not Found
Richa Kushwaha,w2YURGwAAAAJ
Prateek Kumar Soni,Not Found
Mr. Megh Singhal,Not Found
Niveditta Batra,Not Found
Prakhar Mishra,Not Found
Anuja Shukla,Not Found
Ritika Chaudhary,53wFTCsAAAAJ
Mayuri Gupta,Cu0Sof4AAAAJ
""".splitlines()

filtered = [line for line in data if not line.endswith("Not Found")]
for line in filtered:
    print(line)
