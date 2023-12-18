import pytest
import aiohttp
import asyncio

API_URL = "http://localhost:8080"
auth_token = "40a4c44d54a295ec2b19534d16beaa7ccba1557dc9e192bc33c9839d"
@pytest.mark.asyncio
async def test_add_user():
	async with aiohttp.ClientSession() as session:
		payload = {"Username_User": "testuser", "Password_User": "123", "Email_User": "nesolek@gmail.com", "Is_Admin_User": "false"}
		async with session.post(f"{API_URL}/addUser", json=payload) as response:
			assert response.status == 200

@pytest.mark.asyncio
async def test_get_all_monitors():
	async with aiohttp.ClientSession() as session:
		async with session.get(f"{API_URL}/allMonitors", headers={"Authorization": auth_token}) as response:
			assert response.status == 200

@pytest.mark.asyncio
async def test_remove_monitor():
	async with aiohttp.ClientSession() as session:
		async with session.delete(f"{API_URL}/removeMonitor", data="1", headers={"Authorization": auth_token}) as response:
			assert response.status == 200
@pytest.mark.asyncio
async def test_add_display():
	async with aiohttp.ClientSession() as session:
		payload = {"diagonal": "123", "resolsution": "124", "type": "oled", "gsync": "false"}
		async with session.post(f"{API_URL}/addDisplay", json=payload, headers={"Authorization": auth_token}) as response:
			assert response.status == 200
