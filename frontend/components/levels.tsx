import { useRouter } from "next/navigation";
import { Card, CardContent } from "./ui/card";
import { useForm } from "react-hook-form";
import { zodResolver } from "@hookform/resolvers/zod";
import z from "zod";
import { usePostLevelMutation } from "@/hooks/mutations/use-post-level-mutation";
import { useToast } from "./ui/use-toast";

const Levels = () => {
  const router = useRouter();
  const { toast } = useToast();
  const levels = ["🥔 Beginner", "🤺 Intermediate", "🏆 Advanced"];

  const levelmap = new Map<string, string>([
    ["🥔 Beginner", "beginner"],
    ["🤺 Intermediate", "intermediate"],
    ["🏆 Advanced", "advanced"]
  ]);

  const levelMutation = usePostLevelMutation({
    onSuccess: (data, variables) => {
      toast({title: "Selected level", description: "You have selected the level" + variables.level})
      console.log("success");
      router.push("/home");
    },
    onError(error, variables, context) {
      console.log(error);
      console.log(variables);
      console.log(context);
    },
  });

  // const handleSubmit;

  return (
    <Card className="col min-h-[40vh] justify-center">
      {levels.map((item: string) => {
        {
          return (
            <Card key={item} className="m-2" onClick={() => {levelMutation.mutate({level: levelmap.get(item)!});}}>
              <CardContent className="font-bold w-55 text-3xl text-center p-2">
                {item}
              </CardContent>
            </Card>
          );
        }
      })}
    </Card>
  );
};

export default Levels;
