import logo from './logo.svg';
import './App.css';
import { Box, Button } from '@chakra-ui/react';
import { useEffect, useState } from 'react';
import ListUser from './Pages/ListUser';
import AddUser from './Pages/AddUser';

function App() {
  const [state,setstate]=useState(false)
console.log('s',state);
  useEffect(()=>{

  },[state])
  return (
    <div className="App">
    <Box w='40%' margin='auto' mt='50px' display='flex' justifyContent={'space-evenly'}>
      <Button  onClick={()=>setstate(false)}  bg='gray' color='white' _hover={{bg:'blue.500'}}>User List</Button>
      <Button onClick={()=>setstate(true)} bg='gray' color='white' _hover={{bg:'blue.500'}}>Add User</Button>

    </Box>

    {!state?<ListUser/>:<AddUser/>}
    </div>
  );
}

export default App;
