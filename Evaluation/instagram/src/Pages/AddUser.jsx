import { Box, Button, Input } from '@chakra-ui/react'
import React, { useState } from 'react'
import axios from 'axios'
const AddUser = () => {
    const [name,setname]=useState('')
    const adduserdata = () => {
        let obj={
            name
        }
     try {
        axios.post(`http://localhost:8080/users`,obj)
        .then((res)=>alert('User Successfully Added !!'))
        setname('')
     } catch (error) {
        console.log(error)
     }
    }
    return (

        <>
            <Box border='1px solid gray' w='30%' margin='auto' mt='30px' padding='20px'>
                <Input value={name} onChange={(e)=>setname(e.target.value)} placeholder='Enter Your Username' />
                <Button onClick={adduserdata} width={'100%'} mt='15px' _hover={{ bg: 'gray.800', color: 'white' }}>Add User</Button>
            </Box>
        </>
    )
}

export default AddUser
