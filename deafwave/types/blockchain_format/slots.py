from dataclasses import dataclass
from typing import Optional

from blspy import G2Element

from deafwave.types.blockchain_format.proof_of_space import ProofOfSpace
from deafwave.types.blockchain_format.sized_bytes import bytes32
from deafwave.types.blockchain_format.vdf import VDFInfo, VDFProof
from deafwave.util.ints import uint8, uint64
from deafwave.util.streamable import Streamable, streamable


@dataclass(frozen=True)
@streamable
# The hash of this is used as the challenge_hash for the ICC VDF
class ChallengeBlockInfo(Streamable):
    proof_of_space: ProofOfSpace
    # Only present if not the first sp
    challenge_chain_sp_vdf: Optional[VDFInfo]
    challenge_chain_sp_signature: G2Element
    challenge_chain_ip_vdf: VDFInfo


@dataclass(frozen=True)
@streamable
class ChallengeChainSubSlot(Streamable):
    challenge_chain_end_of_slot_vdf: VDFInfo
    # Only at the end of a slot
    infused_challenge_chain_sub_slot_hash: Optional[bytes32]
    # Only once per sub-epoch, and one sub-epoch delayed
    subepoch_summary_hash: Optional[bytes32]
    # Only at the end of epoch, sub-epoch, and slot
    new_sub_slot_iters: Optional[uint64]
    # Only at the end of epoch, sub-epoch, and slot
    new_difficulty: Optional[uint64]


@dataclass(frozen=True)
@streamable
class InfusedChallengeChainSubSlot(Streamable):
    infused_challenge_chain_end_of_slot_vdf: VDFInfo


@dataclass(frozen=True)
@streamable
class RewardChainSubSlot(Streamable):
    end_of_slot_vdf: VDFInfo
    challenge_chain_sub_slot_hash: bytes32
    infused_challenge_chain_sub_slot_hash: Optional[bytes32]
    deficit: uint8  # 16 or less. usually zero


@dataclass(frozen=True)
@streamable
class SubSlotProofs(Streamable):
    challenge_chain_slot_proof: VDFProof
    infused_challenge_chain_slot_proof: Optional[VDFProof]
    reward_chain_slot_proof: VDFProof
