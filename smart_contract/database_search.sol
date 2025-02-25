// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract database_search {
    // array of passwords hashes using SHA256
    bytes32[] private hashes;
    // string[] public user_password_list;

    event Password(string password);
    event PasswordMatchEvent(bytes32 hash);

    constructor() {
        // user_password_list = _user_password_list;
        hashes.push(0x596773d096d51b98f9a2598048bb91d13d2ef85dd603990b2470efae940c48df);
        hashes.push(0x36bf8ba0e3241b35a57f8561d17bf9f82f5372c4907f2054417ebf8b9c422f97);
        hashes.push(0x5140a407d009953e4232aec8dfc1c8dd82374dc5736ca36090017173957f7bdd);
        hashes.push(0x1fcc0254325d85a025e7e66f5f42674f4b1cfcc0beb62fcc03a8ac334a53dea4);
        hashes.push(0xbffc463591e5f18de9b4463a1e3fbe09abac43400d44c97b400dec20a18219ef);
        hashes.push(0x44d66ef19e4ba4b16e87cac5fe249663c02917bc97f82afb4fb54c07a9b6ce82);
        hashes.push(0xc1a4bc5a84392807c0987e51d5b5c0d2f4eb1c8d6885ae03aa629a1ca2254edf);
    }


    function searchDatabaseTest(string[] memory _user_passwords) public {
        for (uint i = 0; i < _user_passwords.length; i++) 
        {
            string memory password = _user_passwords[i];
            bytes memory data = bytes(password);
            bytes32 hash = sha256(data);
            for (uint j = 0; j < hashes.length; j++){
                if (hashes[j] == hash){
                    emit PasswordMatchEvent(hash);
                    emit Password(password);
                }
            }
        }
    }

    function searchDatabase(bytes32[] memory _user_hashes) public {
        for (uint i = 0; i < _user_hashes.length; i++) 
        {
            bytes32 hash = _user_hashes[i];
            for (uint j = 0; j < hashes.length; j++){
                if (hashes[j] == hash){
                    emit PasswordMatchEvent(hash);
                }
            }
        }
    }

    

}