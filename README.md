# TMDT2022

Nhóm đề tài 2 sử dụng docker để ảo hóa server ubuntu

Thành viên:
Phạm Mạnh Đình - 17110122
Đoàn Văn Đức - 17110126

CÁC BƯỚC THỰC HIỆN





TẠO MÁY CHỦ ẢO EC2 INSTANCE UBUNTU 22.04 TRÊN AMAZON AWS

Cần chuẩn bị: Một tài khoản AWS
Tất cả các thành lập sau đây là Free tier cho phép bạn sử dụng miễn phí dịch vụ trong hạn mức nhất định do AWS quy định.
Các bước để tạo một Ubuntu Instance trong AWS:
o	Bước 1: Đăng nhập bằng tải khoản AWS của bạn và đi đến bảng điều khiển.
o	Bước 2: Nhấn vào biểu tượng Services, tìm kiếm EC2 bấm chọn.
o	Bước 3: Phía trên góc phải của trang Amazon EC2, bấm chọn Region (vùng) mà bạn muốn tạo EC2 Instance. Ở đây, mình nhắn chọn vùng Asia Pacific (Singapore) vì máy chủ ở đây gần Việt Nam nhất nên chúng sẽ cho tốc độ truyền tải thông tin nhanh.
 <img width="468" alt="image" src="https://user-images.githubusercontent.com/46060483/202843093-00e5ea40-23f6-4bbb-955e-9013a57262c2.png">

o	Bước 4: Bấm chọn Launch Instance ở EC2 Dashboard.
 
o	Bước 5: (Không bắt buộc) Name and Tags: ở đây chúng ta có thể gắn vài tag cho EC2 Instance. Nhấn chọn Add additional tags, điền name tags bạn muốn thêm vào.
 
 
o	Bước 5: Chọn mục Application and OS Images ( Amazon Machine Image):
-	Quick Start: chọn biểu tượng hệ điều hành Ubuntu.
-	Amazon Machine Image: Chọn Ubuntu Server 22.04 LTS (HVM), SSD Volume Type. Bởi vì có Free tier eligible.
-	Architecture: 64-bit(x86).
 
o	Bước 6: Chọn Instance Type. Ở đây mình sẽ chọn General purpose t2.micro. Bởi vì có Free tier eligible.
 
o	Bước 7: Chọn Key pair (login) để kết nối với EC2 Instance từ máy cục bộ. Nhấn chọn create new key pair để tạo các cặp khóa cho phép bạn kết nối an toàn với phiên bản của mình.
 
Nhập tên của cặp khóa bên dưới đây. Khi được nhắc, hãy lưu khóa cá nhân ở một vị trí an toàn và có thể truy cập được trên máy tính của bạn. Bạn sẽ cần nó sau này để kết nối với phiên bản của bạn.
 
Nhấn chọn Create key pair để tạo cặp khóa, chúng sẽ được download về, như hình bên dưới.
 
o	Bước 8: Chọn Network settings để cấu hình Security Group. Ở đây, chúng ta có thể tạo mới nhóm bảo mật (Sercurity Group) và định nghĩa các cổng (Port) sẽ được mở cho EC2 Instance. Về mặt cơ bản, chúng ta sẽ thêm cổng HTTP, HTTPS và SSH cho EC2 Instance. HTTP và HTTPS là để cho phép các yêu cầu trình duyệt từ khắp nơi trên thế giới đến máy chủ ảo của chúng ta. Và SSH là để kết nối với EC2 Instance từ máy cục bộ của chúng ta. Nhấn chọn Edit, ở đây mình sẽ cấu hình như sau: 
 
-	VPC: Chọn default (mặc định).
-	Subnet: Chọn vùng ap-southeast.
-	Auto-assign public: Enables
-	Firewall (security groups): Create security group.
-	Security group name:  ec2-ubuntu-test.
	
	


 
	Inbound security groups rules:
-	HTTP		80	Anywhere 0.0.0.0/0
-	HTTPS		443	Anywhere 0.0.0.0/0
-	SSH		22	Anywhere or Custom 0.0.0.0/0
Đối với SSH, khuyến khích các bạn nên custom bằng cách cầu hình như sau: <Your Public IP Address>/32 – Cho phép kết nối đến EC2 Instance chỉ duy nhất từ Public IP Address của máy cục bộ của bản. Với đề tài mình sẽ chọn Anywhere, vì nhóm có 3 bạn connect nên sẽ cần kết nối bất kỳ nơi nào.
  
 
o	Bước 9: Chọn Configure storage, ở đây chúng ta có thể thay đổi kích thước dung lượng cho EC2 Instance. Free Tier có thể áp dụng cho dung lượng tối đa 30GB.
 
	Nhấn chọn Advanced để sửa đổi, điền kích thước dung lượng tối đa là 20 GB. Theo mặc định là 8GB, bạn cần nâng lên 20 đến 30 GB để tạo không gian lưu trữ được nhiều dữ liệu hơn.
 

o	Bước 10: Cuối cùng bấm chọn Launch Instance.

 

EC2 Instance của bạn đã sẳn sàng để sử dụng. Hãy chờ một lúc cho đến khi trạng thái của Instance (Instance State) đổi từ running sang status check. Bây giờ bạn có thể kết nối với EC2 Instance từ máy cục bộ của bạn.
 
 
![image](https://user-images.githubusercontent.com/46060483/202843011-a47b0e8a-400a-491c-8730-15cac2422262.png)
