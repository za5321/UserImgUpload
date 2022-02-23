## 📷 **_User Image Upload Batch_**
---

This system calls _'UsrImgUpload'_ API of IF system and then, sends POST request of employee's profile images.<br/><br/>
📝Processes:<br/>
1. Select employee's name and id from Employee table.
2. Access the directory of employees' profile images in the server.
3. Convert the image to hexadecimal values.
4. Encrypt values - _accesstoken, company_id, employee_id, employee_name, hex image value_ - to encryption algorithm. (In this case, I should use **_JPype_** to use java module for encryption that IF system provides.)
5. Send POST request to IF API 

🔧 Requirements:
* Pymssql: Connect Database - SQL Server (MS-SQL). My MS-SQL version is 2016.<br/>
`pip install pymssql`
