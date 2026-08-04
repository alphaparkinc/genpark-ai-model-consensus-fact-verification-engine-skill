from client import AiModelConsensusFactVerificationEngineClient

def main():
    client = AiModelConsensusFactVerificationEngineClient()
    res = client.verify_claim("Water freezes at 0 degrees Celsius at 1 atm pressure", ["ModelA", "ModelB", "ModelC"])
    print(f"Verdict: {res['verdict']} (Consensus: {res['consensus_score_pct']}%)")

if __name__ == "__main__":
    main()
