import asyncio

async def grab_banner(reader,writer):
    
    try:
        writer.write(b"GET / HTTP/1.1\r\nHost: test\r\n\r\n")
        await writer.drain()
        
        banner = await asyncio.wait_for(reader.read(1024),timeout=1)
        
        banner = banner.decode(erros="ignore").strip()
        
        return banner if banner else None 
    
    except:
        return None