import unittest
import requests

class TestBaiduGeocodingAPI(unittest.TestCase):
    BASE_URL = "http://api.map.baidu.com"
    API_KEY = "VPZOC3ftpvigaIbEuZCynhCthA21qyun"

    def test_geocoding_nuaa_address(self):
        endpoint = f"{self.BASE_URL}/geocoding/v3/"
        params = {
            "address": "南京市江宁区将军大道29号",
            "output": "json",
            "ak": self.API_KEY
        }
        response = requests.get(endpoint, params=params)
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data['status'], 0)
        self.assertIn("location", data['result'])
        self.assertIn("lat", data['result']['location'])
        self.assertIn("lng", data['result']['location'])
        print(f"Latitude: {data['result']['location']['lat']}, Longitude: {data['result']['location']['lng']}")

    def test_reverse_geocoding_nuaa_coordinates(self):
        # 假设从上一个测试中得到了南京航空航天大学的经纬度坐标
        latitude = "31.9371"  # 替换为实际返回的纬度
        longitude = "118.794"  # 替换为实际返回的经度
        endpoint = f"{self.BASE_URL}/reverse_geocoding/v3/"
        params = {
            "location": f"{latitude},{longitude}",
            "output": "json",
            "ak": self.API_KEY
        }
        response = requests.get(endpoint, params=params)
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data['status'], 0)
        self.assertIn("result", data)
        self.assertIn("formatted_address", data['result'])
        print(f"Address: {data['result']['formatted_address']}")

    def test_ip_location_near_nuaa(self):
        endpoint = f"{self.BASE_URL}/location/ip"
        params = {
            "ip": "218.94.69.34",  # 假设这个IP地址接近南京航空航天大学
            "ak": self.API_KEY,
            "coor": "bd09ll"
        }
        response = requests.get(endpoint, params=params)
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data['status'], 0)
        self.assertIn("content", data)
        self.assertIn("address", data['content'])
        self.assertIn("point", data['content'])
        print(f"Location: {data['content']['address']}")


if __name__ == "__main__":
    unittest.main()
