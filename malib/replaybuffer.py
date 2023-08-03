import torch
import numpy as np


# class ReplayBuffer:
#     def __init__(self, args):
#         self.s = np.zeros((args.batch_size, args.agent_num, args.state_dim))
#         self.a = np.zeros((args.batch_size, args.agent_num, args.action_dim))
#         self.a_logprob = np.zeros((args.batch_size, args.agent_num, args.action_dim))
#         self.r = np.zeros((args.batch_size, args.agent_num, 1))
#         self.s_ = np.zeros((args.batch_size, args.agent_num, args.state_dim))
#         self.dw = np.zeros((args.batch_size, args.agent_num, 1))
#         self.done = np.zeros((args.batch_size, 1))
#         self.count = 0
#         self.device = args.device
#         self.args = args

#     def store(self, s, a, a_logprob, r, s_, dw, done):
#         if self.count == self.args.batch_size:
#             return
#         self.s[self.count] = s
#         self.a[self.count] = a
#         self.a_logprob[self.count] = a_logprob
#         self.r[self.count] = r
#         self.s_[self.count] = s_
#         self.dw[self.count] = dw
#         self.done[self.count] = done
#         self.count += 1

#     def numpy_to_tensor(self):
#         s = torch.tensor(self.s, dtype=torch.float, device=self.device)
#         a = torch.tensor(self.a, dtype=torch.float, device=self.device)
#         a_logprob = torch.tensor(self.a_logprob, dtype=torch.float, device=self.device)
#         r = torch.tensor(self.r, dtype=torch.float, device=self.device)
#         s_ = torch.tensor(self.s_, dtype=torch.float, device=self.device)
#         dw = torch.tensor(self.dw, dtype=torch.float, device=self.device)
#         done = torch.tensor(self.done, dtype=torch.float, device=self.device)

#         return s, a, a_logprob, r, s_, dw, done
    
class SharedReplayBuffer:
    def __init__(self, args):
        self.s = np.zeros((args.batch_size, args.agent_num, args.state_dim))
        self.cent_s = np.zeros((args.batch_size, args.agent_num, args.share_state_dim))
        self.a = np.zeros((args.batch_size, args.agent_num, args.action_dim))
        self.a_logprob = np.zeros((args.batch_size, args.agent_num, args.action_dim))
        self.r = np.zeros((args.batch_size, args.agent_num, 1))
        self.s_ = np.zeros((args.batch_size, args.agent_num, args.state_dim))
        self.cent_s_ = np.zeros((args.batch_size, args.agent_num, args.share_state_dim))
        self.dw = np.zeros((args.batch_size, args.agent_num, 1))
        self.done = np.zeros((args.batch_size, 1))
        self.count = 0
        self.device = args.device
        self.args = args

    def store(self, s, cent_s, a, a_logprob, r, s_, cent_s_, dw, done):
        if self.count == self.args.batch_size:
            return
        self.s[self.count] = s
        self.cent_s[self.count] = cent_s
        self.a[self.count] = a
        self.a_logprob[self.count] = a_logprob
        self.r[self.count] = r
        self.s_[self.count] = s_
        self.cent_s_[self.count] = cent_s_
        self.dw[self.count] = dw
        self.done[self.count] = done
        self.count += 1

    def numpy_to_tensor(self):
        s = torch.tensor(self.s, dtype=torch.float, device=self.device)
        cent_s = torch.tensor(self.cent_s, dtype=torch.float, device=self.device)
        a = torch.tensor(self.a, dtype=torch.float, device=self.device)
        a_logprob = torch.tensor(self.a_logprob, dtype=torch.float, device=self.device)
        r = torch.tensor(self.r, dtype=torch.float, device=self.device)
        s_ = torch.tensor(self.s_, dtype=torch.float, device=self.device)
        cent_s_ = torch.tensor(self.cent_s_, dtype=torch.float, device=self.device)
        dw = torch.tensor(self.dw, dtype=torch.float, device=self.device)
        done = torch.tensor(self.done, dtype=torch.float, device=self.device)

        return s, cent_s, a, a_logprob, r, s_, cent_s_, dw, done