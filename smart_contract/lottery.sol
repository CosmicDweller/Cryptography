// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract lottery {
    address public owner;
    address[] public participants;
    address public winner;
    uint256 public ticket_price;
    event ParticipantAdded(address participant);
    event WinnerSelected(address winner);

    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can call this function");
        _;
    }

    construct(unit256 _durationInBlock, unint256 _ticket_price) {
        owner = msg.sender;
        endBlock = block.number + _durationInBlocks;
        ticket_price = _ticket_price * 1000000000;
    }

    function optIn() external payable   {
        require(block.number < endBlock, "Lottery opting-in phase is over");
        require(msg.value % ticket_price == 0 && msg.value > 0, "Must pay for exactly one or more tickets to enroll");
        uint256 number_of_tickets_purchased = msg.value / ticket_price;

        for (uint256 i = 0; i < number_of_tickets_purchased; i++) {           
            participants.push(msg.sender);
        }

        emit ParticipantAdded(msg.sender);
    }

    function selectWinner() public onlyOwner {
        require(participants.length > 0, "No participants in the lottery");
        require(block.number >= endBlock, "Opting-in phase is ongoing");

        uint256 randomIndex = _generateRandomNumber() % participants.length;
        winner = participants[randomIndex];

        (bool success, ) = winner.call{value: address(this).balance}("");
        require(success, "Transfer to winner failed");

        emit WinnerSelected(winner);

    }

    function _generateRandomNumber() private view returns (uint256) {
        return uint256(keccak256(abi.encodePacked(block.timestamp, block.prevrandao, participants.length)));
    }
}
