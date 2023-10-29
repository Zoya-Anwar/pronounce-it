import { useRouter } from "next/navigation";
import { Card, CardContent } from "./ui/card";
import { usePostLevelMutation } from "@/hooks/mutations/use-post-level-mutation";
import { useToast } from "./ui/use-toast";

const Levels = () => {
  const router = useRouter();
  const { toast } = useToast();
  const levels = ["🥔 Beginner", "🤺 Intermediate", "🏆 Advanced"];

  const levelmap = new Map<string, string>([
    ["🥔 Beginner", "beginner"],
    ["🤺 Intermediate", "intermediate"],
    ["🏆 Advanced", "advanced"],
  ]);

  const levelMutation = usePostLevelMutation({
    onSuccess: (data, variables) => {
      toast({
        title: "Selected level",
        description: "You have selected the level" + variables.level,
      });
      console.log("success");
      router.push("/home");
    },
    onError(error, variables, context) {
      console.log(error);
      console.log(variables);
      console.log(context);
      toast({
        title: "Error",
        description: "Something went wrong",
        variant: "destructive",
      });
    },
  });

  return (
    <Card className="flex flex-col col min-h-[40vh] min-w-[30vw] justify-around align-middle backdrop-filter backdrop-blur-sm bg-opacity-10 bg-gray-500 border-gray-100 p-8">
      {levels.map((item: string) => {
        {
          return (
            <Card
              key={item}
              className="m-2 hover:bg-gray-100 hover:text-gray-900 cursor-pointer"
              onClick={() => {
                levelMutation.mutate({ level: levelmap.get(item)! });
              }}
            >
              <CardContent className="font-bold w-55 text-3xl text-center p-2 min-h-56">
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
