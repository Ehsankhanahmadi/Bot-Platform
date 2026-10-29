import asyncio 
from assignments.service import ( assign_bot, get_assignment, remove_assignment, ) 



async def main(): 
    print(await assign_bot(8718447220, "runtime-01")) 
    print(await get_assignment(8718447220)) 
    print(await remove_assignment(8718447220)) 
    print(await get_assignment(8718447220))

asyncio.run(main())