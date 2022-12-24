# TMDT2022

## Nhóm đề tài 2 sử dụng docker để ảo hóa server ubuntu

<p>Thành viên</p>
<p>Phạm Mạnh Đình - 17110122</p>
<p>Nguyễn Thế Đoàn - 17110124</p>
<p>Đoàn Văn Đức - 17110126</p>

## Thực hiện xây dựng website có các chức năng: khởi tạo container, tắt container, quản lý user sử dụng container
- Trang website giúp người dùng kết nối tới máy chủ EC2 sau đó thực hiện các chức năng: khởi tạo container, tắt container, quản lý user sử dụng container.
- Người dùng có thể đăng ký tài khoản.
- Admin có thể qug lý người dùng, quản lý các container.
- Các container mà nhóm có thể tạo: container ubuntu, container centos.
- Khi người dùng tạo container có thể lựa chọn server, chọn dung lượng ram, số cpu, ...

## Các bước cài đặt

## Bước 1: Tạo máy chủ ảo EC2 INSTANCE UBUNTU 22.04 TRÊN AMAZON AWS
<p>Cần chuẩn bị: Một tài khoản AWS</p>
<p>Tất cả các thành lập sau đây là Free tier cho phép bạn sử dụng miễn phí dịch vụ trong hạn mức nhất định do AWS quy định.</p>
<p>Các bước để tạo một Ubuntu Instance trong AWS:</p>
- Bước 1: Đăng nhập bằng tải khoản AWS của bạn và đi đến bảng điều khiển.
- Bước 2: Nhấn vào biểu tượng Services, tìm kiếm EC2 bấm chọn
- Bước 3: Phía trên góc phải của trang Amazon EC2, bấm chọn Region (vùng) mà bạn muốn tạo EC2 Instance. Ở đây, mình nhắn chọn vùng Asia Pacific (Singapore) vì máy chủ ở đây gần Việt Nam nhất nên chúng sẽ cho tốc độ truyền tải thông tin nhanh.
<img src="src/Picture1.png"/>
- Bước 4: Bấm chọn Launch Instance ở EC2 Dashboard.
<img src="src/Picture2.png">
- Bước 5: (Không bắt buộc) Name and Tags: ở đây chúng ta có thể gắn vài tag cho EC2 Instance. Nhấn chọn Add additional tags, điền name tags bạn muốn thêm vào.
<img src="src/Picture3.png">
<img src="src/Picture4.png">
- Bước 6: Chọn mục Application and OS Images ( Amazon Machine Image):
-- Quick Start: chọn biểu tượng hệ điều hành Ubuntu.
-- Amazon Machine Image: Chọn Ubuntu Server 22.04 LTS (HVM), SSD Volume Type. Bởi vì có Free tier eligible.
-- Architecture: 64-bit(x86).
<img src="src/Picture5.png">
-- Bước 7: Chọn Instance Type. Ở đây mình sẽ chọn General purpose t2.micro. Bởi vì có Free tier eligible.
<img src="src/Picture6.png">
-- Bước 8: Chọn Key pair (login) để kết nối với EC2 Instance từ máy cục bộ. Nhấn chọn create new key pair để tạo các cặp khóa cho phép bạn kết nối an toàn với phiên bản của mình.
<img src="src/Picture7.png">
<p>Nhập tên của cặp khóa bên dưới đây. Khi được nhắc, hãy lưu khóa cá nhân ở một vị trí an toàn và có thể truy cập được trên máy tính của bạn. Bạn sẽ cần nó sau này để kết nối với phiên bản của bạn.</p>
<img src="src/Picture8.png">
<p>Nhấn chọn Create key pair để tạo cặp khóa, chúng sẽ được download về, như hình bên dưới<p>
<img src="src/Picture9.png">
- Bước 9: Chọn Network settings để cấu hình Security Group. Ở đây, chúng ta có thể tạo mới nhóm bảo mật (Sercurity Group) và định nghĩa các cổng (Port) sẽ được mở cho EC2 Instance. Về mặt cơ bản, chúng ta sẽ thêm cổng HTTP, HTTPS và SSH cho EC2 Instance. HTTP và HTTPS là để cho phép các yêu cầu trình duyệt từ khắp nơi trên thế giới đến máy chủ ảo của chúng ta. Và SSH là để kết nối với EC2 Instance từ máy cục bộ của chúng ta. Nhấn chọn Edit, ở đây mình sẽ cấu hình như sau:
<img src="src/Picture10.png">
-- VPC: Chọn default (mặc định).
-- Subnet: Chọn vùng ap-southeast.
-- Auto-assign public: Enables
-- Firewall (security groups): Create security group.
-- Security group name:  ec2-ubuntu-test.
<p>Inbound security groups rules:</p>
--	HTTP		80	Anywhere 0.0.0.0/0
--	HTTPS		443	Anywhere 0.0.0.0/0
--	SSH		22	Anywhere or Custom 0.0.0.0/0
<img src="src/Picture11.png">
<p>Đối với SSH, khuyến khích các bạn nên custom bằng cách cầu hình như sau: <Your Public IP Address>/32 – Cho phép kết nối đến EC2 Instance chỉ duy nhất từ Public IP Address của máy cục bộ của bản. Với đề tài mình sẽ chọn Anywhere, vì nhóm có 3 bạn connect nên sẽ cần kết nối bất kỳ nơi nào.</p>
<img src="src/Picture12.png">
<img src="src/Picture13.png">
- Bước 10: Chọn Configure storage, ở đây chúng ta có thể thay đổi kích thước dung lượng cho EC2 Instance. Free Tier có thể áp dụng cho dung lượng tối đa 30GB.
<img src="src/Picture14.png">
<p>Nhấn chọn Advanced để sửa đổi, điền kích thước dung lượng tối đa là 20 GB. Theo mặc định là 8GB, bạn cần nâng lên 20 đến 30 GB để tạo không gian lưu trữ được nhiều dữ liệu hơn.</p>
<img src="src/Picture15.png">
- Bước 11: Cuối cùng bấm chọn Launch Instance
<img src="src/Picture16.png">
<p>EC2 Instance của bạn đã sẳn sàng để sử dụng. Hãy chờ một lúc cho đến khi trạng thái của Instance (Instance State) đổi từ running sang status check. Bây giờ bạn có thể kết nối với EC2 Instance từ máy cục bộ của bạn</p>
<img src="src/Picture17.png">
<img src="src/Picture18.png">

## Bước 2: Cài đặt docker trên máy chủ ảo EC2 INSTANCE UBUNTU 22.04 TRÊN AMAZON AWS

<p>Với hệ điều hành Mac OS và Ubuntu thì cách thức và dòng lệnh tương tự nhau nên có thể 
Kết nối qua SSH thường được thực hiện thông qua sự xác thực của public key, yêu cầu người dùng có sẳn Private key của họ. Thông thường chúng ta có thể tạo cặp public key-private key bằng công cụ cửa bên thứ ba và sau đó thêm public key trên Amazon EC2 hoặc một cách khác là từ chính EC2 Instance.</p>
<p>Trong quá trình tạo EC2, sẽ có một bước chọn cặp khóa (Key pair) cho Instance để bạn có thể kết nối với EC2 một cách bảo mật nhất. Bây giờ, chúng ra sẽ SSH đến EC2 Instance Ubuntu từ máy cục bộ của bạn (Mac/Ubuntu).</p>
<p>Các bước kết nối EC2 từ Mac/Ubuntu:</p>
<ul><li>Bước 1: Mở Terminal.</li></ul>
<ul><li>Bước 2: Dẫn đến thư mục nơi chưa file private key (.pem).</li></ul>
<ul><li>Bước 3: Run dòng lệnh với format sau đây để kết nối với EC2 Instance</li></ul>
<p>Cú pháp: sudo ssh -I “private-key-cua-ban.pem” "instance-user-name"@"instance-public-dns-name"</p>
<img src="src/Picture19.png">
<p>Cú pháp nhóm thực hiện: sudo ssh -i "awskey.pem" ubuntu@ec2-13-250-27-131.ap-southeast-1.compute.amazonaws.com
Thay thế "instance-user-name"@"instance-public-dns-name" bằng Hostname và Username của EC2 Instance của bạn. Bạn có thể tìm thấy thông tin này trên bảng điều khiển AWS EC2. Đi tới EC2 Dashboard. Bấm chọn Instances. Tích vào ô Instance mà bạn muốn kết nối, sau đó bấm chọn Connect. Tiếp tục bấm chọn SSH Client. Bạn có thể thấy chi tiết các bước kết nối với EC2 Instance qua SSH mà AWS cũng hướng dẫn.</p>
<img src="src/Picture20.png">
<p>Trước khi SSH, nếu file private (.pem) của bạn đang ở trạng thái public thì trước tiên cần phải run command sau để đảm bảo tính bảo mật của private key.</p>
<p>$ sudo chmod 400 “<private-key-cua-ban>.pem”</p>
<p>Nếu đây là lần đầu tiên bạn kết nối với instance này, nó sẽ hiển thị cảnh báo bảo mật. Nhập yes để tiếp tục kết nối với EC2 Instance.</p>
<img src="src/Picture21.png">
<p>Bây giờ bạn đã có thể kết nối với EC2 Instance từ máy cục bộ của bạn.
Các lỗi thường xảy ra khi SSH đến EC2 Instance:</p>
<p>Connection timed out: ssh: connect to host ec2-X-X-X-X.compute-1.amazonaws.com port 22: connection timed out Thông báo lỗi này xuất phát từ SSH Client. Lỗi này cho biết EC2 Instance không phản hồi với máy cục bộ và kết nối hết thời gian chờ. Sau đây là các nguyên nhân phổ biến gây ra lỗi này:</p>
<ul>
<li>Security group không cho phép kết nối. Đối với trường hợp này, bạn hãy xem lại port 22 trong security group của EC2 Instance có cho phép kết nối từ Public IP Address của bạn hay chưa.</li>
<li>Tưởng lửa (firewall) đã được bật trên EC2 Instance. Đối với trường hợp này, bạn nên đảm bảo rằng sẽ không có tường lửa ngăn chặn kết nối giữa Instance và máy cục bộ.</li>
<li>Hostname IP address của server không tồn tại. Đối với trường hợp này, bạn nên kiểm tra lại hostname hay IP address đã trùng khớp hay chưa.</li>
</ul>
<p>Permision denied: Permission denied (publickey,gssapi-keyex,gssapi-with-mic) đây là một trong những lỗi phổ biến khi kết nối SSG với Instance. Vì vậy phải đảm bảo private key mà bạn sử dụng trong quá trình kết nối SSH và cặp khóa bạn đã chọn trước đó phải trùng khớp. nếu chúng không khớp, bạn sẽ nhận lỗi như trên.</p>

## Bước 3: Kết nối Ubuntu EC2 với Visual studio code trên máy tính cục bộ (máy tính cá nhân)
<p>Trong phần này, mình hướng dẫn các bạn cách kết nối VS Code IDE (Visual studio code IDE) cụ bộ của bạn với phiên bản EC2 đang chạy trong mạng con riêng tư bằng cách sử dụng trình quản lý phiên AWS Systems Manager và Đăng nhập một lần AWS (SSO).</p>
<p>Điều này rất hữu ích khi bạn muốn tận dụng các chức năng của phiên bản EC2, đồng thời có kinh nghiệm phát triển dự án.</p>
<p>Các điều kiện tiên quyết: cài đặt phần mềm Visual studio code IDE, đã thiết lập tạo máy chủ ảo EC2 Instance Ubuntu 22.04 trên Amazon AWS (mục 1), cài đặt Remote Developmnet extention trong visual stuido code (như hình).</p>
<img src="src/Picture32.png">
<br>
<img src="src/Picture33.png">
<br>
<img src="src/Picture34.png">
<br>
<img src="src/Picture35.png">
<p>Thêm các dòng sau vào ~/.ssh/config tập tin của bạn:</p>
<ul>
<li>Host: Bạn có thể đặt tên theo ý của bạn.</li>
<li>Host Name: Địa chỉ IP mà bạn Public (như hình trên)</li>
<li>IdentityFile: Đưa đường dẫn đến file .pem</li>
</ul>
<img src="src/Picture36.png">
<br>
<img src="src/Picture37.png">
<br>
<img src="src/Picture38.png">
<p>Thao tác này sẽ mở trình duyệt mặc định của bạn và bắt đầu quá trình đăng nhập cho tài khoản AWS của bạn. Thực hiện theo các bước trên trình duyệt của bạn để cho phép cấp ủy quyền.</p>
<ul>
<li>Nếu không kết nối thành công (hết thời gian chờ), có thể là do độ trễ lâu khi để cho phép yêu cầu ủy quyền. Trong trường hợp này chỉ cần nhấp yêu cầu thử lại (Retry) và cho phép yêu cầu trên trình duyệt (hiển thị bên dưới)</li>
<li>Nếu bạn bị quyền từ chối (khóa công khai) permission denied (publickey), bạn phải nhập lệnh sau: chmod 400 awskey.pem (lưu ý: theo tên file .pem, bạn có thể xem ở mục 2 kết nối ssh và coppy lại lệnh đó để thực hiện)  để đảm bảo khóa thể hiện công khai. Lệnh này phải thực thi trong tập thu mục chưa file .pem của bạn.</li>
</ul>
<img src="src/Picture39.png">
<p>Bây giờ, bạn sẽ được kết nối với EC2 và có thể mở các thư mục trên EC2 giống như cách bạn làm đối với mã cục bộ của mình.</p>
<img src="src/Picture40.png">
<br>
<img src="src/Picture41.png">
<br>
<img src="src/Picture42.png">
<br>

## Bước 4: Lập trình webiste python django - docker - ec2

<img src="src/Picture22.jpg">
<br>
<img src="src/picture24.jpg">
<br>
<img src="src/picture25.jpg">
<br>
<img src="src/picture26.jpg">
<br>
<img src="src/picture27.jpg">
<br>
<img src="src/picture29.jpg">
<br>
<img src="src/picture30.jpg">
<br>
<img src="src/picture31.jpg">
