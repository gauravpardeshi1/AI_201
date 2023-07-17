import { Box, Button, Heading, Image, Text } from '@chakra-ui/react'
import axios from 'axios'
import React, { useEffect, useState } from 'react'

const ListUser = () => {
    const[data,setdata]=useState([])
    const [update,setupdate]=useState(false)
    const[like,setlike]=useState(0)
    const handledelete=(id)=>{
        // console.log('i',id)
        axios.delete(`http://localhost:8080/users/${id}`)
        alert('User Successfully Deleted !!')
        setupdate(!update)
    }
    const handlelike=(id)=>{
        
    }
    useEffect(()=>{
        axios.get(`http://localhost:8080/users`)
        .then((res)=>setdata(res.data))
    },[update])
  return (
    <div>
      <Box border='1px solid gray' w='30%' margin='auto' h='auto' mt='30px' padding='20px'>
      {data && data.map((e)=><Box display='flex' gap='20px' alignItems={'center'} mt='15px'>
        <Image w='40%' h='50%' src={'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRiibOngFYog5Ri5UoFKH3CsHMOvomBLf4JAw&usqp=CAU'}/>
      <Box>   
      <Heading fontSize={20} fontWeight={500}>Username : ${e.name}</Heading>
      <Text _hover={{cursor:'pointer'}} fontSize={20} fontWeight={500} onClick={()=>handlelike(e.id)}>Likes : {like}</Text>
        <Button mt='10px' onClick={()=>handledelete(e.id)}>Delete</Button>
        </Box> 
      </Box>)}
      </Box>
    </div>
  )
}

export default ListUser
