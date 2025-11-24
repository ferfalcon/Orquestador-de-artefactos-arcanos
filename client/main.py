from models import Artifact, RiskLevel
from menu import show_menu

# -------------------------------------------------------------------
# Data input
# -------------------------------------------------------------------
def register_artifact(artifacts: list[Artifact]):
    print("\n=== Register New Artifact ===")
    name = input("Artifact name: ").strip()

    risk_level = input_risk_level()
    tasks = input_tags()

    artifact = Artifact(name=name, risk_level=risk_level, tags=tasks)
    artifacts.append(artifact)

    print(f"\n✅ Artifact '{artifact.name}' registered.")


def input_risk_level() -> RiskLevel:
    print("\nSelect risk level:")
    options = list(RiskLevel)
    for index, level in enumerate(options, start=1):
        print(f"{index}. {level.value}")

    while True:
        choice = input("Enter number: ").strip()
        if not choice.isdigit():
            print("Please enter a number.")
            continue

        index = int(choice)
        if 1 <= index <= len(options):
            return options[index - 1]
        else:
            print("Invalid option, try again.")


def input_tags() -> list[str]:
    print("\nEnter tasks for this artifact.")
    print("Separate tasks with commas, e.g.: open portal, summon shades")
    raw = input("Tasks: ").strip()

    if not raw:
        return []

    taks = [task.strip() for task in raw.split(",") if task.strip()]
    return taks


# -------------------------------------------------------------------
# Functions
# -------------------------------------------------------------------

def list_artifacts(artifacts: list[Artifact]):
    print("\n=== Artifact Catalog ===")

    if not artifacts:
        print("No artifacts registered yet.")
        return

    for i, artifact in enumerate(artifacts, start=1):
        print(f"\n[{i}] {artifact.name}")
        print(f"   Risk level: {artifact.risk_level.value}")
        if artifact.tags:
            print("   Tasks:")
            for task in artifact.tags:
                print(f"     - {task}")
        else:
            print("   Tasks: (none)")


def delete_artifact(artifacts: list[Artifact]):
    print("\n=== Delete Artifact ===")

    if not artifacts:
        print("There are no artifacts to delete.")
        return

    for i, artifact in enumerate(artifacts, start=1):
        print(f"[{i}] {artifact.name} (risk: {artifact.risk_level.value})")

    while True:
        choice = input("Enter the number of the artifact to delete (or 'c' to cancel): ").strip()

        if choice.lower() == "c":
            print("Deletion cancelled.")
            return

        if not choice.isdigit():
            print("Please enter a valid number or 'c' to cancel.")
            continue

        index = int(choice)

        if not (1 <= index <= len(artifacts)):
            print(f"Please enter a number between 1 and {len(artifacts)}, or 'c' to cancel.")
            continue

        artifact = artifacts.pop(index - 1)
        print(f"❌ Artifact '{artifact.name}' has been deleted.")
        return


# -------------------------------------------------------------------
# Main
# -------------------------------------------------------------------
def main():
    artifacts: list[Artifact] = []

    while True:
        show_menu()
        choice = input("Choose an option: ").strip()

        if choice == "1":
            register_artifact(artifacts)
        elif choice == "2":
            list_artifacts(artifacts)
        elif choice == "3":
            delete_artifact(artifacts)
        elif choice == "4":
            print("Goodbye, keep your artifacts warded.")
            break
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()
